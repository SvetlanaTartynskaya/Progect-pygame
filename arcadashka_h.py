import pygame
import random
import sqlite3

# инициализация pygame
pygame.init()

# настройки экрана
screen_width = 1280
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Аркада')

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# настройки платформы
platform_width = 150
platform_height = 40
platform_x = screen_width // 2 - platform_width // 2
platform_y = screen_height - platform_height - 10
platform_speed = 5

# настройки шарика
ball_radius = 15
ball_speed_x = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
ball_speed_y = -4
ball_x = screen_width // 2
ball_y = screen_height // 2

# настройки прямоугольников
rectangle_width = 80
rectangle_height = 20
rectangle_speed = 2
rectangle_count = 20
rectangles = []

# создаем прямоугольники
for i in range(rectangle_count):
    x = random.randint(0, screen_width - rectangle_width)
    y = random.randint(50, screen_height - rectangle_height - 50)
    rectangle = pygame.Rect(x, y, rectangle_width, rectangle_height)  # исправил опечатку в названии класса
    rectangles.append(rectangle)

# счетчик
counter = 0

# цикл игры
game_over = False  # исправил опечатку в названии переменной
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # исправил опечатку в названии события
            game_over = True

    # движение платформы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:  # исправил опечатку в названии клавиш
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x < screen_width - platform_width:  # исправил опечатку в названии клавиш
        platform_x += platform_speed

    # движение шарика и проверка выхода за экран
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x < ball_radius or ball_x > screen_width - ball_radius:  # проверяем выход за границы по оси x
        ball_speed_x = -ball_speed_x
    if ball_y < ball_radius:  # проверяем выход за границу по оси y
        ball_speed_y = -ball_speed_y
    elif ball_y > screen_height:  # проверяем выход за нижнюю границу по оси y
        game_over = True

    # проверка столкновения шарика с платформой
    if ball_y > platform_y - ball_radius and platform_x - ball_radius < ball_x < platform_x + platform_width - ball_radius:
        ball_speed_y = -ball_speed_y

    # проверка столкновения шарика с прямоугольником
    for rectangle in rectangles:
        if rectangle.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            rectangles.remove(rectangle)
            counter += 1
            ball_speed_y = -ball_speed_y

    # проверка победы
    if counter >= 12:
        # открытие окна с результатами
        result_screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Сюжет')

        # фраза по середине
        font = pygame.font.Font(None, 46)
        result_text = font.render('Что вы заметили в этой комнате?', True, white)
        result_text_rect = result_text.get_rect()
        result_text_rect.center = (screen_width // 2, screen_height // 2 - 200)

        # кнопки
        button1 = pygame.Rect(screen_width // 2 - 320, screen_height // 2 + 50, 700, 60)
        button2 = pygame.Rect(screen_width // 2 - 320, screen_height // 2 + 150, 700, 60)
        button_font = pygame.font.Font(None, 36)
        button_text1 = button_font.render('Маньяк взял нож, как орудие убийства', True, black)
        button_text2 = button_font.render('Нож упал случайно', True, black)
        button_text_rect1 = button_text1.get_rect()
        button_text_rect2 = button_text2.get_rect()
        button_text_rect1.center = button1.center
        button_text_rect2.center = button2.center

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button1.collidepoint(mouse_pos):
                        sqlite3.Cursor.execute('''INSERT INTO chooses (room3) VALUES (1)''')
                        sqlite3.Connection.commit()
                        pygame.quit()
                        exit()
                    elif button2.collidepoint(mouse_pos):
                        sqlite3.Cursor.execute("INSERT INTO chooses (room3) VALUES (-1)")
                        sqlite3.Connection.commit()
                        done = True
                        pygame.quit()
                        exit()

            result_screen.fill(black)
            result_screen.blit(result_text, result_text_rect)
            pygame.draw.rect(result_screen, white, button1)
            pygame.draw.rect(result_screen, white, button2)
            result_screen.blit(button_text1, button_text_rect1)
            result_screen.blit(button_text2, button_text_rect2)
            pygame.display.flip()

    # обновление экрана
    screen.fill(black)
    pygame.draw.rect(screen, white, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    for rectangle in rectangles:
        pygame.draw.rect(screen, white, rectangle)

    pygame.display.flip()

    clock.tick(100)

# закрытие pygame
pygame.quit()
