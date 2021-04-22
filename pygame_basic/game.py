import pygame

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Test game")
# background = pygame.image.load("C:\Users\케이지케이\Documents\practice\game\pygame_basic\background.jpg")
character = pygame.image.load("https://www.flaticon.com/svg/vstatic/svg/3885/3885025.svg?token=exp=1619081421~hmac=9f4bd262dddec45be649b11af322333e")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


#Even roof
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((0,0,130))
  # screen.blit(background, (0,0))
  screen.blit(character, (character_x_pos,character_y_pos))
  pygame.display.update()

pygame.quit()