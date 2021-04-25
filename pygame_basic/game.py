import pygame

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Avoiding game")

#FPS
clock = pygame.time.Clock()

#background image
background = pygame.image.load("background.jpg")

#character
character = pygame.image.load("character.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#Move
to_x = 0
character_speed = 0.6

#enemy
enemy = pygame.image.load("enemy.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = 0
enemy_y_pos = 0
enemy_speed = 10


game_font = pygame.font.Font(None, 40)

total_time = 10
start_ticks = pygame.time.get_ticks()

#Even roof
running = True
while running:
  dt = clock.tick(30)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT:
        to_x += character_speed

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0

#position of character
character_x_pos += to_x *dt

#가로
if character_x_pos < 0:
  character_x_pos = 0
elif character_x_pos > screen_width - character_width:
  character_x_pos = screen_width - character_width

#position of enemy
enemy_y_pos += enemy_speed


#collision
character_rect = character.get_rect()
character_rect.left = character_x_pos
character_rect.right = character_y_pos

enemy_rect = enemy.get_rect()
enemy_rect.left = enemy_x_pos
enemy_rect.right = enemy_y_pos

if character_rect.colliderect(enemy_rect):
  print("Bump!")
  running = False

  

  screen.blit(background, (0,0))
  screen.blit(character, (character_x_pos,character_y_pos))
  screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

  elapsed_time = (pygame.time.get_ticks() - start_ticks)/ 1000
  timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
  screen.blit(timer, (10,10))

  if total_time - elapsed_time <= 0:
    print("Time out")
    running = False

  pygame.display.update()

pygame.time.delay(2000)
pygame.quit()