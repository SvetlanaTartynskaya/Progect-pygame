import pygame
import random

# инициализируем размеры окна и сетки игрового поля
width = 1280
height = 1024
grid_width = 10
grid_height = 20

# инициализируем размер каждой ячейки на игровом поле
cell_size = 30

# инициализируем цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
orange = (255, 165, 0)

# инициализируем начальные координаты для текущей фигуры
initial_x = grid_width // 2 - 1
initial_y = 0

# инициализируем формы фигур и их цвета
shapes = [
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
]
shape_colors = [
    yellow,
    cyan,
    magenta,
    orange,
    green,
    red,
    blue,
]

# функция для создания пустой сетки
def create_grid():
    grid = [[black for _ in range(grid_width)] for _ in range(grid_height)]
    return grid

# функция для отрисовки сетки
def draw_grid(screen, grid):
    for row in range(grid_height):
        for col in range(grid_width):
            pygame.draw.rect(screen, grid[row][col], (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, white, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

# функция для отрисовки фигуры
def draw_shape(screen, shape, color, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                pygame.draw.rect(screen, color, ((x + col) * cell_size, (y + row) * cell_size, cell_size, cell_size))
                pygame.draw.rect(screen, black, ((x + col) * cell_size, (y + row) * cell_size, cell_size, cell_size), 1)

# функция для проверки столкновения фигуры с границами сетки и уже установленными фигурами
def check_collision(grid, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                if x + col < 0 or x + col >= grid_width or y + row >= grid_height or grid[y + row][x + col] != black:
                    return True
    return False

# функция для поворота фигуры
def rotate_shape(shape):
    return list(zip(*reversed(shape)))

# функция для удаления заполненных строк и смещения остальных фигур вниз
def clear_rows(grid):
    full_rows = []
    for row in range(grid_height):
        if all(cell != black for cell in grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [black] * grid_width)
    return len(full_rows)

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("tetris")

    clock = pygame.time.Clock()

    game_over = False

    # создаем сетку и текущую фигуру
    grid = create_grid()
    current_shape = random.choice(shapes)
    current_color = random.choice(shape_colors)
    current_x, current_y = initial_x, initial_y

    lines_cleared = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(grid, current_shape, current_x - 1, current_y):
                        current_x -= 1

                if event.key == pygame.K_RIGHT:
                    if not check_collision(grid, current_shape, current_x + 1, current_y):
                        current_x += 1

                if event.key == pygame.K_DOWN:
                    if not check_collision(grid, current_shape, current_x, current_y + 1):
                        current_y += 1

                if event.key == pygame.K_SPACE:
                    rotated_shape = rotate_shape(current_shape)
                    if not check_collision(grid, rotated_shape, current_x, current_y):
                        current_shape = rotated_shape

                # добавлена возможность поворота фигуры на 90 градусов с помощью кнопок 'a' и 'd'
                if event.key == pygame.K_UP:
                    rotated_shape = rotate_shape(current_shape)
                    for _ in range(3):
                        if not check_collision(grid, rotated_shape, current_x, current_y):
                            current_shape = rotated_shape
                            rotated_shape = rotate_shape(current_shape)
                        else:
                            break

        if not check_collision(grid, current_shape, current_x, current_y + 1):
            current_y += 1
        else:
            for row in range(len(current_shape)):
                for col in range(len(current_shape[0])):
                    if current_shape[row][col] == 1:
                        if current_y + row <= 0:  # проверяем, если соприкоснулся с верхней границей экрана
                            game_over = True
                        grid[current_y + row][current_x + col] = current_color
                        if lines_cleared >= 10:
                            game_over = True

            # очищаем заполненные строки и увеличиваем счетчик очищенных строк
            lines_cleared += clear_rows(grid)

            # выбираем новую случайную фигуру и цвет
            current_shape = random.choice(shapes)
            current_color = random.choice(shape_colors)
            current_x, current_y = initial_x, initial_y

        # отрисовываем игровое поле и текущую фигуру
        screen.fill(black)
        draw_grid(screen, grid)
        draw_shape(screen, current_shape, current_color, current_x, current_y)

        # отображаем количество очищенных строк в правом верхнем углу
        font = pygame.font.Font(None, 36)
        text = font.render("Кол-во строк: " + str(lines_cleared), True, white)
        screen.blit(text, (width - text.get_width() - 10, 10))

        font = pygame.font.Font(None, 36)
        text = font.render(f'Вам нужно набрать 10 строк.', True, white)
        screen.blit(text, (width - text.get_width() - 10, 45))

        pygame.display.flip()
        clock.tick(7)

    pygame.quit()

if __name__ == "__main__":
    main()
