# Importing stuffs
import pygame, time
from pygame._sdl2 import Window

# Initialize Pygame
pygame.init()
# Get display info for future display related stuff
display_info = pygame.display.Info()
# Set window size to max display size and get width and height for future uses
window_size = (display_info.current_w, display_info.current_h)
width = display_info.current_w
height = display_info.current_h
# Caption that shi, need to add icon
pygame.display.set_caption("Zombie shooter")
# Set screen to size of monitor, scaled for element scaling with different size resolutions
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.SCALED)
window = Window.from_display_module()
# No mouse bc have my own crosshair
pygame.mouse.set_visible(False)
right_click = False
# Anchor window top left
window.position = (0,0)
# Custom full screen toggle
small_screen = False
# Pygame clock
clock = pygame.time.Clock()
# Game is running
running = True
# Delta time, for physics or sum ?
dt = 0
# Start player in the middle of the screen
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# If running main loop
while running:
    # pygame quit is when click on X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill screen with greenish colour to remove any unneeded stuff
    screen.fill("gray58")
    # Get key presses
    keys = pygame.key.get_pressed()
    # Shift toggle for sprinting
    shift_held = False
    # Mouse for crosshair
    mouse_pos = pygame.mouse.get_pos()
    # Player circle with skin tone-ish colour
    pygame.draw.circle(screen, pygame.Color(255, 206, 180), player_pos, radius=10)
    # Draw line from player to mouse. This is temporary just to see if I could, future plan is to somehow use this to get gun sight line and fov
    # Temporary if not j toggle for line toggle when j is held down
    if not keys[pygame.K_j]:
        pygame.draw.line(screen, "white", [player_pos.x, player_pos.y], mouse_pos, 3)
    # Get x and y from mouse_pos and then draw 2 lines onto given x and y making crosshair
    x, y = mouse_pos
    pygame.draw.line(screen, (0, 0, 0), (x - 10, y), (x + 10, y), 3)
    pygame.draw.line(screen, (0, 0, 0), (x, y - 10), (x, y + 10), 3)
    if pygame.mouse.get_pressed()[2]:
        # If right click is held, draw over crosshair and draw dot over everything
        # TODO Find better way to cover crosshair other than drawing over with background colour bc this could lead to drawing over player or other objects
        pygame.draw.circle(screen, pygame.Color(148, 148, 148), mouse_pos, radius=12)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), mouse_pos, radius=3)
    # Mouse button click draws circle around mouse
    if pygame.mouse.get_pressed()[0]:
        # Left click draws circle around to mouse just to show that I can
        pygame.draw.circle(screen, pygame.Color(0, 255, 0), mouse_pos, radius=30, width=3)
    if keys[pygame.K_f]:
        # Custom full screen toggle
        if not small_screen:
            # If screen is big, changes to small and makes resizable sleep at end just in case F is held down
            width, height = 960, 540
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            small_screen = True
            pygame.display.flip()
            time.sleep(0.25)
        else:
            # If screen is small set to maximum resolution and remove frame, basically replicating fullscreen without fullscreen blacking screen out when toggling to and from
            # Another window position is needed to anchor top left when toggling to fullscreen in case window gets moved
            window.position = (0, 0)
            screen = pygame.display.set_mode(window_size, pygame.NOFRAME)
            pygame.display.flip()
            small_screen = False
            time.sleep(0.25)
    if keys[pygame.K_LSHIFT]:
        # Sprint toggle, adds red circle onto to player to show that is shifting, that is temporary
        pygame.draw.circle(screen, "red", player_pos, 5)
        shift_held = True
    if keys[pygame.K_ESCAPE]:
        # Click escape to close game, useful for fullscreen closing
        running = False
    # All movement, 2 instances : just key and key with shift, dk if there is a better way to make this so will have to research
    if keys[pygame.K_w] and shift_held:
        player_pos.y -= 250 * dt
    if keys[pygame.K_w]:
        player_pos.y -= 150 * dt
    if keys[pygame.K_s] and shift_held:
        player_pos.y += 250 * dt
    if keys[pygame.K_s]:
        player_pos.y += 150 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 150 * dt
    if keys[pygame.K_a] and shift_held:
        player_pos.x -= 250 * dt
    if keys[pygame.K_d]:
        player_pos.x += 150 * dt
    if keys[pygame.K_d] and shift_held:
        player_pos.x += 250 * dt
    # Update screen after everything
    pygame.display.flip()
    # clock.tick for frame rate, delta time for physics ?
    dt = clock.tick(60) / 1000

pygame.quit()
