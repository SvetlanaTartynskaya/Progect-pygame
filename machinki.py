from random import randint
import pygame
import sys

# инициализация библиотеки pygame.
pygame.init()

# установка таймера событий каждую секунду.
pygame.time.set_timer(pygame.USEREVENT, 1000)

# определение цветов.
black = (0, 0, 0)
red = (255, 215, 0)

# размеры окна.
width = 550
height = 400

# загрузка изображений машин.
cars = ('car2.jpg', 'car3.jpg', 'car4.jpg')
cars_surf = []

# создание окна.
pov = pygame.display.set_mode((width, height))

# текст после окончания игры.
font = pygame.font.Font(None, 70)
text = font.render("game over!", True, red)
place = text.get_rect(center=(width // 2, height // 2))
pov.blit(text, place)
pygame.display.update()

# загрузка изображений машин.
for i in range(len(cars)):
    cars_surf.append(pygame.image.load(cars[i]).convert_alpha())

# класс для машин.
class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed = randint(1, 3)

    def update(self):
        if self.rect.y < height:
            self.rect.y += self.speed
        else:
            self.kill()

# класс для управляемой машины.
class UserCar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('car.jpg').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(width // 2, height - 10))

# группа для хранения машин.
cars_group = pygame.sprite.Group()

# создание случайной машины.
Car(randint(1, width), cars_surf[randint(0, 2)], cars_group)

# создание управляемой машины.
user_car = UserCar()

# флаг для проверки продолжения игры.
play = True
game_over_lose = False
game_over_win = False

# загрузка фона.
road = pygame.image.load('road.jpg')

# счетчик времени и флаг для проверки достижения 40 секунд.
time_counter = 0

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            # появление новых машин.
            Car(randint(1, width), cars_surf[randint(0, 2)], cars_group)
    
    # отрисовка фона.
    pov.blit(road, [-128, 0])

    # отрисовка и обновление машин.
    cars_group.draw(pov)
    cars_group.update()

    # обработка нажатий клавиш.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        user_car.rect.x -= 2
    elif keys[pygame.K_RIGHT]:
        user_car.rect.x += 2
    
    pov.blit(user_car.image, user_car.rect)

    pygame.display.update()
    pygame.time.delay(10)
    
    # проверка на столкновение с машинами.
    if pygame.sprite.spritecollideany(user_car, cars_group):
        play = False
        game_over_lose = True
        pov.blit(text, place)
        pygame.display.update()
        pygame.time.delay(20)

    time_counter += 1

    if time_counter >= 2000:
        play = False
        game_over_win = True


if game_over_lose:
    pov.fill(black)
    text = font.render("Вы проиграли!", True, red)
    place = text.get_rect(center=(width // 2, height // 2))
    pov.blit(text, place)
    pygame.display.update()
    pygame.time.delay(400)

if game_over_win:
    pov.fill(black)
    text = font.render("Вы прошли дальше!", True, red)
    place = text.get_rect(center=(width // 2, height // 2))
    pov.blit(text, place)
    pygame.display.update()
    pygame.time.delay(400)