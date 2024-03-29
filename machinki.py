from random import randint
import pygame

# инициализация библиотеки pygame.
pygame.init()

# установка таймера событий каждую секунду.
pygame.time.set_timer(pygame.USEREVENT, 1000)

win = False

# определение цветов.
black = (0, 0, 0)
red = (255, 215, 0)

# размеры окна.
w = 550
h = 400

font = pygame.font.Font(None, 70)

# загрузка изображений машин.
cars = ('car2.jpg', 'car3.jpg', 'car4.jpg')
cars_surf = []

# создание окна.
pov = pygame.display.set_mode((w, h))

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
        if self.rect.y < h:
            self.rect.y += self.speed
        else:
            self.kill()


# класс для управляемой машины.
class UserCar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('car.jpg').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(w // 2, h - 10))


# группа для хранения машин.
cars_group = pygame.sprite.Group()

# загрузка фона.
road = pygame.image.load('road.jpg')


def main():
    play = True
    game_over_win = False
    game_over_lose = False
    font = pygame.font.Font(None, 70)
    pov = pygame.display.set_mode((w, h))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    Car(randint(1, w), cars_surf[randint(0, 2)], cars_group)
    user_car = UserCar()
    time_counter = 0
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.USEREVENT:
                # появление новых машин.
                Car(randint(1, w), cars_surf[randint(0, 2)], cars_group)

        # отрисовка фона.
        pov.blit(road, [-128, 0])

        # отрисовка и обновление машин.
        cars_group.draw(pov)
        cars_group.update()

        # обработка нажатий клавиш.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and user_car.rect.x > 0:
            user_car.rect.x -= 2
        if keys[pygame.K_RIGHT] and user_car.rect.bottomright[0] < w:
            user_car.rect.x += 2
        if keys[pygame.K_UP] and user_car.rect.y > (h // 2):
            user_car.rect.y -= 2
        if keys[pygame.K_DOWN] and user_car.rect.bottomright[1] < h:
            user_car.rect.y += 2

        pov.blit(user_car.image, user_car.rect)

        pygame.display.update()
        pygame.time.delay(10)

        if game_over_win:
            win = True
            pov.fill(black)
            text = font.render("Вы прошли дальше!", True, red)
            place = text.get_rect(center=(w // 2, h // 2))
            pov.blit(text, place)
            pygame.display.update()
            pygame.time.delay(400)
            play = False

        # проверка на столкновение с машинами.
        if pygame.sprite.spritecollideany(user_car, cars_group):
            game_over_lose = True
            if game_over_lose:
                play = False
                pov.fill(black)
                text = font.render("Вы проиграли!", True, red)
                place = text.get_rect(center=(w // 2, h // 2))
                pov.blit(text, place)
                pygame.display.update()
                cars_group.empty()
                pygame.time.delay(400)

        time_counter += 1

        if time_counter >= 2000:
            win = True
