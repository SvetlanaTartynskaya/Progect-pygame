import pygame
import sys
import tetris

from pygame import surface

if __name__ == '__main__':
    # инициализация pygame
    pygame.init()

    # задаем размеры окна
    win_width, win_height = 1280, 1024

    # создаем окно
    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("потом название придумаем")

    # загрузка фоновых изображений комнат
    room_1_image = pygame.image.load("game.room1.png").convert()
    room_2_image = pygame.image.load("game.room2.png").convert()
    room_3_image = pygame.image.load("game.room3.png").convert()
    room_4_image = pygame.image.load("game.room4.png").convert()
    room_5_image = pygame.image.load("game.room5.png").convert()
    room_6_image = pygame.image.load("game.room5.png").convert()

    # создание отдельных экземпляров класса surface для каждой комнаты
    room_1_surface = pygame.surface.Surface((win_width, win_height))
    room_1_surface.blit(room_1_image, (0, 0))

    room_2_surface = pygame.surface.Surface((win_width, win_height))
    room_2_surface.blit(room_2_image, (0, 0))

    room_3_surface = pygame.surface.Surface((win_width, win_height))
    room_3_surface.blit(room_3_image, (0, 0))

    room_4_surface = pygame.surface.Surface((win_width, win_height))
    room_4_surface.blit(room_4_image, (0, 0))

    room_5_surface = pygame.surface.Surface((win_width, win_height))
    room_5_surface.blit(room_5_image, (0, 0))

    room_6_surface = pygame.surface.Surface((win_width, win_height))
    room_6_surface.blit(room_6_image, (0, 0))

    # БД
    conn = sqlite3.connect('chooses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chooses (
                        room11 INT,
                        room12 INT,
                        room21 INT,
                        room22 INT,
                        room3 INT,
                        room41 INT,
                        room42 INT
                    )''')

    # переменная для хранения текущей комнаты
    current_room: surface.Surface = room_1_surface
    room_num = 0
    main_rooms = (room_1_surface, room_2_surface, room_3_surface, room_4_surface)

    screen = pygame.display.set_mode((win_width, win_height))

    # загружаем фон экрана
    background_image = pygame.image.load("start_background.png")

    # загружаем изображение кнопки пуск
    start_button_image = pygame.image.load("start_button.png")

    # загрузка кнопки
    button_rect = start_button_image.get_rect()
    button_rect.topleft = (770, 430)
    screen.blit(background_image, (0, 0))
    screen.blit(start_button_image, (770, 430))

    # первая мини-игра и подсказка
    class button_carpet:
        def __init__(self, position, size):
            self.rect = pygame.Rect(position, size)
            self.clicked = False

        def check_collision(self, mouse_pos):
            if self.rect.collidepoint(mouse_pos):
                self.clicked = True
                self.run_function()
                self.update()

        def update(self):
            # обновление кнопки после нажатия
            if self.clicked:
                # можно добавить изменение внешнего вида кнопки
                pass

        def run_function(self):
            tetris.main()

    button_carpet_position = (38, 845)   # позиция кнопки на поверхности
    button_carpet_size = (50, 50)        # размер кнопки
    button_carpet = button_carpet(button_carpet_position, button_carpet_size)

    # основной игровой цикл
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
            elif event.type == pygame.KEYDOWN:
                # переключение комнат с помощью стрелок
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
                else:
                    if event.button == 1:  # левая кнопка мыши
                        mouse_pos = pygame.mouse.get_pos()
                        button_carpet.check_collision(mouse_pos)

        # обновление экрана
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
