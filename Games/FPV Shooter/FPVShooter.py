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
ammo_boxes = []
enemies_alive = 5
current_wave = 1
max_waves = 3
power_up_cost = 20
damage_cooldown = 0.5  # Time between consecutive damage

# Setup the game world
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(50, 50), collider='box')
Sky(texture='sky_default')

# Player setup
player = FirstPersonController()

# UI Elements
ammo_display = Text(f"Ammo: {ammo_count}", position=(-0.85, 0.45), scale=2, background=True)
health_display = Text(f"Health: {player_health}", position=(-0.85, 0.4), scale=2, background=True)
score_display = Text(f"Score: {player_score}", position=(-0.85, 0.35), scale=2, background=True)
wave_display = Text(f"Wave: {current_wave}/{max_waves}", position=(-0.85, 0.3), scale=2, background=True)
power_up_display = Text("", position=(-0.85, 0.25), scale=2, background=True)

# Enemy setup
def spawn_enemies(wave):
    global enemies, enemies_alive
    enemies_alive = wave * 5  # More enemies per wave
    for _ in range(enemies_alive):
        x = random.randint(-10, 10)
        z = random.randint(5, 25)
        enemy = Entity(model='cube', color=color.yellow, position=(x, 1, z), collider='box', scale=1.5)
        enemies.append(enemy)

spawn_enemies(current_wave)

# Ammo Box setup
def spawn_ammo_box():
    """Spawns a hovering ammo box at a random location."""
    x = random.randint(-10, 10)
    z = random.randint(-10, 10)
    ammo_box = Entity(
        model='cube',
        color=color.green,
        position=(x, 1.5, z),
        scale=(0.5, 0.5, 0.5),
        collider='box'
    )
    ammo_box.animate_position(ammo_box.position + Vec3(0, 0.5, 0), duration=1, curve=curve.linear, loop=True)
    ammo_box.animate_rotation((0, 360, 0), duration=2, curve=curve.linear, loop=True)
    ammo_boxes.append(ammo_box)

# Spawn some initial ammo boxes
for _ in range(3):
    spawn_ammo_box()

# Shooting mechanics
def shoot():
    global ammo_count, bullets
    if ammo_count > 0:
        try:
            # Create the bullet using the global camera object
            bullet = Entity(
                model='sphere',
                color=color.red,
                scale=(0.2, 0.2, 0.2),
                position=camera.world_position + camera.forward * 2,  # Use global `camera`
                collider='box',
            )
            # Animate the bullet's movement
            bullet.animate_position(bullet.position + (camera.forward * 20), duration=1, curve=curve.linear)
            bullets.append(bullet)
            ammo_count -= 1
            ammo_display.text = f"Ammo: {ammo_count}"

            # Schedule destruction of the bullet
            destroy(bullet, delay=1.5)
        except Exception as e:
            print(f"Error in shoot function: {e}")
    else:
        print("No ammo left!")

# Reload mechanics
def reload():
    global ammo_count
    ammo_count = 10
    ammo_display.text = f"Ammo: {ammo_count}"

# Power-up mechanics
def activate_power_up():
    global ammo_count, player_score
    if ammo_count >= power_up_cost:
        ammo_count -= power_up_cost
        ammo_display.text = f"Ammo: {ammo_count}"
        for enemy in enemies:
            destroy(enemy)
        enemies.clear()
        power_up_display.text = "Power-Up Activated!"
        player_score += 50 * enemies_alive
        score_display.text = f"Score: {player_score}"

# Update enemy behavior and player status
last_damage_time = time.time()

def update():
    global player_health, enemies, bullets, ammo_boxes, enemies_alive, current_wave, player_score, last_damage_time

    # Enemy AI: Move toward the player
    for enemy in enemies:
        if distance(enemy, player) < 20:
            enemy.position += (player.position - enemy.position).normalized() * time.dt * 2

        # Check if enemy hits player
        if distance(enemy, player) < 1.5 and time.time() - last_damage_time > damage_cooldown:
            player_health -= 1
            last_damage_time = time.time()
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

    # Check if player touches an ammo box
    for ammo_box in ammo_boxes:
        if distance(ammo_box, player) < 2:
            ammo_count += 5
            ammo_display.text = f"Ammo: {ammo_count}"
            destroy(ammo_box)
            ammo_boxes.remove(ammo_box)

# Input handling
def input(key):
    if key == 'shift':  # Use Shift to shoot
        print("Attempting to shoot...")
        shoot()
    elif key == 'r':  # Press 'R' to reload
        reload()
    elif key == 'p':  # Press 'P' to activate power-up
        activate_power_up()
    elif key == 'escape':  # Press 'ESC' to quit
        print("Quitting game...")
        application.quit()

# Run the game
app.run()
