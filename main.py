import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))
test_surface.fill((0, 0, 200))

x_pos = 100
y_pos = 100

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        y_pos -= 50

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_d:
        x_pos += 50

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        y_pos += 50

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        x_pos -= 50

  screen.fill(pygame.Color(175, 215, 70))
  # X & Y cooridinates
  screen.blit(test_surface, (x_pos, y_pos))
  pygame.display.update()
  clock.tick(60)
  print('test')