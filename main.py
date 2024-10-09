import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Тестовый проект')

image = pygame.image.load('pyLogo-80.png')
image_rect = image.get_rect()

image2 = pygame.image.load('pyCharm-80.png')
image2_rect = image2.get_rect()

# speed = 1



run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            image_rect.x = mouse_x - 40
            image_rect.y = mouse_y - 40

    if image_rect.colliderect(image2_rect):
        print("Произошло столкновение")
        time.sleep(1)

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image2, image2_rect)
    pygame.display.flip()


pygame.quit()