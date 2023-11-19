import pygame
import sys

# Инициализация pygame
pygame.init()

# Задаем размеры окна
win_width, win_height = 800, 600

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

# Создание отдельных экземпляров класса Surface для каждой комнаты
room_1_surface = pygame.Surface((win_width, win_height))
room_1_surface.blit(room_1_image, (0, 0))

room_2_surface = pygame.Surface((win_width, win_height))
room_2_surface.blit(room_2_image, (0, 0))

room_3_surface = pygame.Surface((win_width, win_height))
room_3_surface.blit(room_3_image, (0, 0))

room_4_surface = pygame.Surface((win_width, win_height))
room_4_surface.blit(room_4_image, (0, 0))

room_5_surface = pygame.Surface((win_width, win_height))
room_5_surface.blit(room_5_image, (0, 0))

room_6_surface = pygame.Surface((win_width, win_height))
room_6_surface.blit(room_6_image, (0, 0))

# Переменная для хранения текущей комнаты
current_room = room_1_surface

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
                if current_room == room_1_surface:
                    current_room = room_2_surface
                elif current_room == room_2_surface:
                    current_room = room_3_surface
                elif current_room == room_3_surface:
                    current_room = room_4_surface
                elif current_room == room_4_surface:
                    current_room = room_5_surface
                elif current_room == room_5_surface:
                    current_room = room_6_surface
                elif current_room == room_6_surface:
                    current_room = room_1_surface

            elif event.key == pygame.K_LEFT:
                if current_room == room_2_surface:
                    current_room = room_1_surface
                elif current_room == room_3_surface:
                    current_room = room_2_surface
                elif current_room == room_4_surface:
                    current_room = room_3_surface
                elif current_room == room_5_surface:
                    current_room = room_4_surface
                elif current_room == room_6_surface:
                    current_room = room_5_surface
                elif current_room == room_1_surface:
                    current_room = room_6_surface

    # Отрисовка текущей комнаты
    window.blit(current_room, (0, 0))

    # Обновление экрана
    pygame.display.flip()
