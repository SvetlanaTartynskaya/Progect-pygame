import pygame
import sys
import machinki
import Tetris
import arcadashka

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

        # БД
    conn = sqlite3.connect('chooses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chooses (
                        room11 INT,
                        room12 INT,
                        room2 INT,
                        room3 INT,
                        room41 INT,
                        room42 INT
                    )''')

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
    mgbutton1_rect = pygame.Rect(38, 845, 100, 100)
    mgbutton2_rect = pygame.Rect(235, 300, 100, 100)
    mgbutton3_rect = pygame.Rect(1055, 955, 100, 100)
    mgbutton4_rect = pygame.Rect(1070, 672, 100, 100)
    mgbutton5_rect = pygame.Rect(495, 430, 100, 100)
    mgbutton6_rect = pygame.Rect(135, 665, 100, 100)
    mgbutton7_rect = pygame.Rect(580, 653, 100, 100)

    tetrisdiff = 0
    arcadediff = 0

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
                if game_start:
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

                    if event.key == pygame.K_DOWN:
                        if current_room == room_5_surface:
                            current_room = main_rooms[room_num]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if button_rect.collidepoint(event.pos):
                    game_start = True
                if game_start:
                    if mgbutton1_rect.collidepoint(event.pos):
                        if current_room == room_1_surface:
                            if tetrisdiff == 0:
                                Tetris.main()
                            else:
                                tetrisdiff -= 1
                                Tetris.easen()
                                Tetris.main()
                    if mgbutton2_rect.collidepoint(event.pos):
                        if current_room == room_1_surface:
                            if arcadediff == 0:
                                arcadashka.main()
                            else:
                                arcadediff -= 1
                                arcadashka.easen()
                                arcadashka.main()
                    if mgbutton3_rect.collidepoint(event.pos):
                        if current_room == room_2_surface:
                            machinki.main()
                    if mgbutton4_rect.collidepoint(event.pos):
                        if current_room == room_2_surface:
                            if tetrisdiff == 1:
                                Tetris.main()
                            elif tetrisdiff > 1:
                                tetrisdiff -= 1
                                Tetris.easen()
                                Tetris.main()
                            else:
                                tetrisdiff += 1
                                Tetris.harden()
                                Tetris.main()
                    if mgbutton5_rect.collidepoint(event.pos):
                        if current_room == room_3_surface:
                            if arcadediff == 1:
                                arcadashka.main()
                            elif arcadediff > 1:
                                arcadediff -= 1
                                arcadashka.easen()
                                arcadashka.main()
                            else:
                                arcadediff += 1
                                arcadashka.harden()
                                arcadashka.main()
                    if mgbutton6_rect.collidepoint(event.pos):
                        if current_room == room_4_surface:
                            if tetrisdiff == 2:
                                Tetris.main()
                            elif tetrisdiff > 2:
                                tetrisdiff -= 1
                                Tetris.easen()
                                Tetris.main()
                            else:
                                tetrisdiff += 1
                                Tetris.harden()
                                Tetris.main()
                    if mgbutton7_rect.collidepoint(event.pos):
                        if current_room == room_4_surface:
                            if arcadediff == 2:
                                arcadashka.main()
                            elif arcadediff > 2:
                                arcadediff -= 1
                                arcadashka.easen()
                                arcadashka.main()
                            else:
                                arcadediff += 1
                                arcadashka.harden()
                                arcadashka.main()
                    window = pygame.display.set_mode((win_width, win_height))
                    pygame.display.set_caption("Потом название придумаем")
        # Обновление экрана
        pygame.display.flip()
    pygame.quit()
