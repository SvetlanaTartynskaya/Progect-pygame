import pygame
import random

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cube Escape")

# Класс для сцены
class Scene:
    def __init__(self, text):
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_render = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
    def show(self):
        screen.fill(BLACK)
        screen.blit(self.text_render, self.text_rect)
        pygame.display.flip()
        
    def handle_event(self, event):
        pass

# Класс для сцены с кнопкой
class ButtonScene(Scene):
    def __init__(self, text, next_scene):
        super().__init__(text)
        self.next_scene = next_scene
        
    def show(self):
        super().show()
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50))
        button_font = pygame.font.Font(None, 24)
        button_text = button_font.render("Нажмите здесь", True, BLACK)
        button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))
        screen.blit(button_text, button_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if (WIDTH // 2 - 100 < mouse_pos[0] < WIDTH // 2 + 100 and
                        HEIGHT // 2 + 50 < mouse_pos[1] < HEIGHT // 2 + 100):
                    scenes.remove(self)
                    scenes.append(self.next_scene)

# Создание сцен
start_scene = Scene("Начало игры")
story_scene = ButtonScene("Сюжетное окно", Scene("Сюжетная линия"))
additional_scene = ButtonScene("Дополнительное окно", Scene("Дополнительная сцена"))
game_scene = Scene("Основное игровое поле")

# Список сцен
scenes = [start_scene, story_scene, additional_scene, game_scene]

# Главный игровой цикл
running = True
current_scene = scenes[0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_scene.handle_event(event)
        
    current_scene.show()

pygame.quit()