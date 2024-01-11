import pygame
import sys

from pygame import Surface

if __name__ == '__main__':
    # Инициализация pygame
    pygame.init()

    # Задаем размеры окна
    win_width, win_height = 1280, 1024

    # Создаем окно
    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Потом название придумаем")

    # Загрузка фоновых изображений комнат
    room_1_image = pygame.image.load("game.room1.png").convert()
    room_2_image = pygame.image.load("game.room2.png").convert()
    room_3_image = pygame.image.load("game.room3.png").convert()
    room_4_image = pygame.image.load("game.room4.png").convert()
    room_5_image = pygame.image.load("game.room5.png").convert()
    room_6_image = pygame.image.load("game.room5.png").convert()

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
    current_room: Surface = room_1_surface
    room_num = 0
    main_rooms = (room_1_surface, room_2_surface, room_3_surface, room_4_surface)

    screen = pygame.display.set_mode((win_width, win_height))

    # Загружаем фон экрана
    background_image = pygame.image.load("start_background.png")

    # Загружаем изображение кнопки пуск
    start_button_image = pygame.image.load("start_button.png")

    # Загрузка кнопки
    button_rect = start_button_image.get_rect()
    button_rect.topleft = (770, 430)
    screen.blit(background_image, (0, 0))
    screen.blit(start_button_image, (770, 430))

    # Основной игровой цикл
    running = True
    game_start = False
    while running:
        if game_start:
            window.blit(current_room, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Переключение комнат с помощью стрелок
                if event.key == pygame.K_RIGHT:
                    if current_room in main_rooms:
                        room_num += 1
                    if room_num > 3:
                        room_num = 0
                    current_room = main_rooms[room_num]

                if event.key == pygame.K_LEFT:
                    if current_room in main_rooms:
                        room_num -= 1
                    if room_num < 0:
                        room_num = 3
                    current_room = main_rooms[room_num]

                if event.key == pygame.K_UP:
                    if current_room in main_rooms:
                        current_room = room_5_surface
                    elif current_room == room_6_surface:
                        current_room = main_rooms[room_num]

                if event.key == pygame.K_DOWN:
                    if current_room in main_rooms:
                        current_room = room_6_surface
                    elif current_room == room_5_surface:
                        current_room = main_rooms[room_num]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_start = True

        # Обновление экрана
        pygame.display.flip()
    pygame.quit()
