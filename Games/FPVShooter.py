from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the game window
app = Ursina()

# Setup the game world
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(50, 50), collider='box')
walls = [
    Entity(model='cube', scale=(5, 5, 1), position=(5, 2.5, 0), color=color.gray, collider='box'),
    Entity(model='cube', scale=(5, 5, 1), position=(-5, 2.5, 10), color=color.gray, collider='box'),
]

# Add a sky texture
Sky(texture='sky_default')

# Player setup
player = FirstPersonController()

# Ammo system
ammo_count = 10
ammo_display = Text(f"Ammo: {ammo_count}", position=(-0.85, 0.45), scale=2, background=True)

# Shooting mechanics
bullets = []

def shoot():
    global ammo_count
    if ammo_count > 0:
        bullet = Entity(
            model='cube',
            color=color.red,
            scale=(0.2, 0.2, 0.2),
            position=player.camera.world_position + player.camera.forward * 2,
            collider='box',
        )
        bullet.animate_position(bullet.position + (player.camera.forward * 20), duration=1, curve=curve.linear)
        bullets.append(bullet)
        ammo_count -= 1
        ammo_display.text = f"Ammo: {ammo_count}"

# Reload mechanics
def reload():
    global ammo_count
    ammo_count = 10
    ammo_display.text = f"Ammo: {ammo_count}"

# Enemy setup
enemies = [Entity(model='cube', position=(x, 1, x * 2), color=color.yellow, collider='box') for x in range(3, 8)]

# Enemy movement
def update():
    for enemy in enemies:
        if distance(enemy, player) < 5:
            enemy.position += (player.position - enemy.position).normalized() * time.dt * 2

    # Check for bullet-enemy collision
    for bullet in bullets:
        if bullet.intersects().hit:
            hit_entity = bullet.intersects().entity
            if hit_entity in enemies:
                enemies.remove(hit_entity)
                destroy(hit_entity)
            destroy(bullet)

    # End game condition
    if len(enemies) == 0:
        Text("You Win!", scale=3, origin=(0, 0), background=True)
        application.pause()

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
