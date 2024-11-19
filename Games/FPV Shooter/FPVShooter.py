from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# Initialize the game
app = Ursina()

# Game Variables
ammo_count = 10
player_health = 100
player_score = 0
enemies = []
bullets = []
healing_boxes = []
enemies_alive = 5
current_wave = 1
max_waves = 3
damage_cooldown = 0.5  # Time between taking damage
healing_amount = 20  # Amount of health the healing box restores

# Setup the game world
ground = Entity(model='plane', scale=(100, 1, 100), texture='white_cube', texture_scale=(50, 50), collider='box')
Sky(texture='sky_default')

# Player setup
player = FirstPersonController()

# UI Elements
ammo_display = Text(f"Ammo: {ammo_count}", position=(-0.85, 0.45), scale=2, background=True)
health_display = Text(f"Health: {player_health}", position=(-0.85, 0.4), scale=2, background=True)
score_display = Text(f"Score: {player_score}", position=(-0.85, 0.35), scale=2, background=True)
wave_display = Text(f"Wave: {current_wave}/{max_waves}", position=(-0.85, 0.3), scale=2, background=True)

# Enemy setup
def spawn_enemies(wave):
    global enemies, enemies_alive
    enemies_alive = wave * 5  # More enemies per wave
    for _ in range(enemies_alive):
        x = random.randint(-40, 40)
        z = random.randint(5, 90)
        enemy = Entity(model='cube', color=color.yellow, position=(x, 1, z), collider='box', scale=1.5)
        enemies.append(enemy)

spawn_enemies(current_wave)

# Healing box setup
def spawn_healing_box():
    x = random.randint(-40, 40)
    z = random.randint(-40, 40)
    healing_box = Entity(
        model='cube',
        color=color.green,
        position=(x, 1, z),
        collider='box',
        scale=(1, 1, 1),
    )
    healing_boxes.append(healing_box)

# Spawn some initial healing boxes
for _ in range(5):
    spawn_healing_box()

# Shooting mechanics
def shoot():
    global ammo_count
    if ammo_count > 0:
        bullet = Entity(
            model='sphere',
            color=color.red,
            scale=(0.2, 0.2, 0.2),
            position=player.position + (0, 1.5, 0),
            collider='box',
        )
        bullet.animate_position(bullet.position + (player.forward * 50), duration=1, curve=curve.linear)
        bullets.append(bullet)
        ammo_count -= 1
        ammo_display.text = f"Ammo: {ammo_count}"

# Reload mechanics
def reload():
    global ammo_count
    ammo_count = 10
    ammo_display.text = f"Ammo: {ammo_count}"

# Update enemy behavior and player status
def update():
    global player_health, enemies, bullets, enemies_alive, current_wave, player_score

    # Enemy AI: Move toward the player
    for enemy in enemies:
        if distance(enemy, player) < 20:
            enemy.position += (player.position - enemy.position).normalized() * time.dt * 2

        # Check if enemy hits player
        if distance(enemy, player) < 1.5:
            player_health -= 1
            health_display.text = f"Health: {player_health}"
            if player_health <= 0:
                Text("Game Over!", scale=3, origin=(0, 0), background=True)
                application.pause()

    # Bullet collision with enemies
    for bullet in bullets:
        if bullet.intersects().hit:
            hit_entity = bullet.intersects().entity
            if hit_entity in enemies:
                enemies.remove(hit_entity)
                destroy(hit_entity)
                enemies_alive -= 1
                player_score += 10
                score_display.text = f"Score: {player_score}"
                if enemies_alive == 0 and current_wave < max_waves:
                    current_wave += 1
                    wave_display.text = f"Wave: {current_wave}/{max_waves}"
                    spawn_enemies(current_wave)
                elif enemies_alive == 0 and current_wave == max_waves:
                    Text("You Win!", scale=3, origin=(0, 0), background=True)
                    application.pause()
            destroy(bullet)

    # Check if the player collides with a healing box
    for healing_box in healing_boxes:
        if distance(healing_box, player) < 1.5:
            player_health += healing_amount
            player_health = min(player_health, 100)  # Cap health at 100
            health_display.text = f"Health: {player_health}"
            healing_boxes.remove(healing_box)
            destroy(healing_box)

# Input handling
def input(key):
    if key == 'left mouse down':  # Left-click to shoot
        shoot()
    elif key == 'r':  # Press 'R' to reload
        reload()
    elif key == 'escape':  # Press 'ESC' to quit
        application.quit()

# Run the game
app.run()
