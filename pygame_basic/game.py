import pygame

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Test game")

#FPS
clock = pygame.time.Clock()

# background = pygame.image.load("C:\Users\케이지케이\Documents\practice\game\pygame_basic\background.jpg")
character = pygame.image.load("https://www.flaticon.com/svg/vstatic/svg/3885/3885025.svg?token=exp=1619081421~hmac=9f4bd262dddec45be649b11af322333e")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#Move
to_x = 0
to_y = 0

character_speed = 0.6

enemy = pygame.image.load("enemy.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = screen_height - enemy_height


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
      elif event.key == pygame.K_UP:
        to_y -= character_speed
      elif event.key == pygame.K_DOWN:
        to_y += character_speed
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0

character_x_pos += to_x *dt
character_y_pos += to_y *dt

#가로
if character_x_pos < 0:
  character_x_pos = 0
elif character_x_pos > screen_width - character_width:
  character_x_pos = screen_width - character_width

#세로
if character_y_pos < 0:
  character_y_pos = 0
elif character_y_pos > screen_height - character_height:
  character_y_pos = screen_height - character_height


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

  screen.fill((0,0,130))
  # screen.blit(background, (0,0))
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