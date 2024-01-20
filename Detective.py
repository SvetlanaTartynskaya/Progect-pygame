import pygame
import sys
import sqlite3
import machinki
import tetris
import arcadashka
from pygame import Surface

ending = False
if __name__ == '__main__':
    # Инициализация pygame
    pygame.init()

    # Задаем размеры окна
    screen_width, screen_height = 1280, 1024

    # Создаем окно
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Detective")

    # Загрузка фоновых изображений комнат
    room_1_image = pygame.image.load("game.room1.png").convert()
    room_2_image = pygame.image.load("game.room3.png").convert()
    room_3_image = pygame.image.load("game.room2.png").convert()
    room_4_image = pygame.image.load("game.room4.png").convert()
    room_5_image = pygame.image.load("game.room5.png").convert()

    # Создание отдельных экземпляров класса Surface для каждой комнаты
    room_1_surface = pygame.Surface((screen_width, screen_height))
    room_1_surface.blit(room_1_image, (0, 0))

    room_2_surface = pygame.Surface((screen_width, screen_height))
    room_2_surface.blit(room_2_image, (0, 0))

    room_3_surface = pygame.Surface((screen_width, screen_height))
    room_3_surface.blit(room_3_image, (0, 0))

    room_4_surface = pygame.Surface((screen_width, screen_height))
    room_4_surface.blit(room_4_image, (0, 0))

    room_5_surface = pygame.Surface((screen_width, screen_height))
    room_5_surface.blit(room_5_image, (0, 0))

    # Переменная для хранения текущей комнаты
    current_room: Surface = room_5_surface
    room_num = 2
    main_rooms = (room_2_surface, room_1_surface, room_5_surface, room_4_surface, room_3_surface)

    screen = pygame.display.set_mode((screen_width, screen_height))

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
    mgbutton_rect_end = pygame.Rect(533, 548, 100, 100)

    tetrisdiff = 0
    arcadediff = 0
    con = sqlite3.connect('chooses.db')
    cursor = con.cursor()


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
                        if current_room in main_rooms and room_num < 4:
                            room_num += 1
                            current_room = main_rooms[room_num]

                    if event.key == pygame.K_LEFT:
                        if current_room in main_rooms and room_num > 0:
                            room_num -= 1
                            current_room = main_rooms[room_num]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if button_rect.collidepoint(event.pos):
                    game_start = True
                if game_start:
                    if mgbutton1_rect.collidepoint(event.pos):
                        if current_room == room_1_surface:
                            if tetrisdiff == 0:
                                tetris.main()
                            else:
                                tetrisdiff -= 1
                                tetris.easen()
                                tetris.main()
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
                                tetris.main()
                            elif tetrisdiff > 1:
                                tetrisdiff -= 1
                                tetris.easen()
                                tetris.main()
                            else:
                                tetrisdiff += 1
                                tetris.harden()
                                tetris.main()
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
                                tetris.main()
                            elif tetrisdiff > 2:
                                tetrisdiff -= 1
                                tetris.easen()
                                tetris.main()
                            else:
                                tetrisdiff += 1
                                tetris.harden()
                                tetris.main()
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
                    if mgbutton_rect_end.collidepoint(event.pos):
                        if current_room == room_5_surface:
                            game_start = False
                            ending = True

                    window = pygame.display.set_mode((screen_width, screen_height))
                    pygame.display.set_caption("Detective")
        if ending:
            font = pygame.font.Font(None, 27)
            text = font.render("За дверью была комната. В середине стояло зеркало во весь рост, а над зеркалом выключатель от лампы.",
                               True, 'white')
            text_rect = text.get_rect(topleft=(10, 500))
            text2 = font.render("Я включил свет. Он был не яркий, но всё было видно. В зеркале отражался я.",
                               True, 'white')
            text_rect2 = text.get_rect(topleft=(10, 550))
            text3 = font.render("Я был в крови, мои руки, моё лицо всё было в ней, а на моём пальце было кольцо, кольцо моей давней знакомой.",
                               True, 'white')
            text_rect3 = text.get_rect(topleft=(10, 600))
            text4 = font.render(
                "Рядом с зеркалом лежал нож и драгоценности, в которых умерла старуха и любимый фрак её мужа, перепачканный в крови.",
                True, 'white')
            text_rect4 = text.get_rect(topleft=(10, 650))
            text5 = font.render(
                "Вдруг послышалась ругань полицейских и лай собак. Меня поймали. Так вот почему семья казалась мне грязной, я сам сделал их такими.",
                True, 'white')
            text_rect5 = text.get_rect(topleft=(10, 700))
            window.fill('black')
            window.blit(text, text_rect)
            window.blit(text2, text_rect2)
            window.blit(text3, text_rect3)
            window.blit(text4, text_rect4)
            window.blit(text5, text_rect5)
        # Обновление экрана
        pygame.display.flip()
    pygame.quit()
