import pygame
import sys

# Инициализация pygame
pygame.init()

# Задаем размеры окна
win_width, win_height = 1280, 1024

# Создаем окно
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Потом название придумаем")

# Загрузка фоновых изображений комнат
room_1_image = pygame.image.load("room1.png").convert()
room_2_image = pygame.image.load("room2.jpg").convert()
room_3_image = pygame.image.load("room3.jpg").convert()
room_4_image = pygame.image.load("room4.jpg").convert()
room_5_image = pygame.image.load("room5.jpg").convert()
room_6_image = pygame.image.load("room6.jpg").convert()

# Переменная для хранения текущей комнаты
current_room = room_1_image

# Основной игровой цикл
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Переключение комнат с помощью стрелок
            if event.key == pygame.K_RIGHT:
                if current_room == room_1_image:
                    current_room = room_2_image
                elif current_room == room_2_image:
                    current_room = room_3_image
                elif current_room == room_3_image:
                    current_room = room_4_image
                elif current_room == room_4_image:
                    current_room = room_1_image

            elif event.key == pygame.K_LEFT:
                if current_room == room_2_image:
                    current_room = room_1_image
                elif current_room == room_3_image:
                    current_room = room_2_image
                elif current_room == room_4_image:
                    current_room = room_3_image
                elif current_room == room_1_image:
                    current_room = room_4_image
            
            # С этого момента всё идёт комом

            elif event.key == pygame.K_UP:
                if current_room == room_1_image or room_2_image == current_room or current_room == room_3_image or current_room == room_4_image:
                    current_room = room_5_image

            elif event.key == pygame.K_UP:
                if current_room == room_5_image:
                    current_room = room_3_image

            elif event.key == pygame.K_DOWN:
                if current_room == room_1_image or room_2_image == current_room or current_room == room_3_image or current_room == room_4_image:
                    current_room = room_6_image

            elif event.key == pygame.K_DOWN:
                if current_room == room_6_image:
                    current_room = room_3_image

            elif event.key == pygame.K_DOWN:
                if current_room == room_1_image:
                    current_room = room_6_image
                elif current_room == room_2_image:
                    current_room = room_6_image
                elif current_room == room_3_image:
                    current_room = room_6_image
                elif current_room == room_4_image:
                    current_room = room_6_image
                elif current_room == room_5_image:
                    current_room = room_6_image

    # Отрисовка текущей комнаты
    window.blit(current_room, (0, 0))

    # Обновление экрана
    pygame.display.flip()
