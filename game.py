# Імпорт необхідних бібліотек
from tkinter import Tk, Canvas
from random import shuffle

# Задання констант
# Розмір ігрового поля (4x4)
BOARD_SIZE = 4
# Розмір одного блоку у пікселях
SQUARE_SIZE = 80
# Значення порожнього блоку.
# У нашому випадку порожнім буде останній блок
EMPTY_SQUARE = BOARD_SIZE**2
# Головне вікно
root = Tk()
root.title("Pythonicway Fifteen")
# Область для малювання
canvas = Canvas(
    root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE, bg="#808080"
)
board = list(range(1, EMPTY_SQUARE + 1))


def draw_board():
    # Прибираємо все, що  нарисоване в області для малювання
    canvas.delete("all")
    # Наша задача згрупувати п’ятнашки зі списку у квадрат
    # розміром  BOARD_SIZE x BOARD_SIZE
    # i та j будуть координатами для кожної окремої п’ятнашки
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # Отримуємо значення для його малювання на квадраті
            index = str(board[BOARD_SIZE * i + j])
            # Якщо це не клітинка, яку необхідно залишити порожньою
            if index != str(EMPTY_SQUARE):
                # Малюємо квадрат по заданним координатам
                canvas.create_rectangle(
                    j * SQUARE_SIZE,
                    i * SQUARE_SIZE,
                    j * SQUARE_SIZE + SQUARE_SIZE,
                    i * SQUARE_SIZE + SQUARE_SIZE,
                    fill="#43ABC9",
                    outline="#FFFFFF",
                )
                # Пишемо число у центрі квадрата
                canvas.create_text(
                    j * SQUARE_SIZE + SQUARE_SIZE / 2,
                    i * SQUARE_SIZE + SQUARE_SIZE / 2,
                    text=index,
                    font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                    fill="#FFFFFF",
                )


def get_empty_neighbor(index):
    # получаем индекс пустой клетки в списке
    empty_index = board.index(EMPTY_SQUARE)
    # узнаем расстояние от пустой клетки до клетки по которой кликнули
    abs_value = abs(empty_index - index)
    # Если пустая клетка над или под клектой на которую кликнули
    # возвращаем индекс пустой клетки
    if abs_value == BOARD_SIZE:
        return empty_index
    # Если пустая клетка слева или справа
    elif abs_value == 1:
        # Проверяем, чтобы блоки были в одном ряду
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    # Рядом с блоком не было пустого поля
    return index


def show_victory_plate():
    # Рисуем черный квадрат по центру поля
    canvas.create_rectangle(
        SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
        BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
        fill="#000000",
        outline="#FFFFFF",
    )
    # Пишем красным текст Победа
    canvas.create_text(
        SQUARE_SIZE * BOARD_SIZE / 2,
        SQUARE_SIZE * BOARD_SIZE / 1.9,
        text="ПОБЕДА!",
        font="Helvetica {} bold".format(int(10 * BOARD_SIZE)),
        fill="#DC143C",
    )


def click(event):
    # Зчитуємо координати клика
    x, y = event.x, event.y
    # Конвертуємо координати з пікселів у клітинки
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    # Получаем индекс в списке объекта по которому мы нажали
    board_index = x + (y * BOARD_SIZE)
    # Получаем индекс пустой клетки в списке. Эту функцию мы напишем позже
    empty_index = get_empty_neighbor(board_index)
    # Меняем местами пустую клетку и клетку, по которой кликнули
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    # Перемальовуємо ігрове поле
    draw_board()
    # Если текущее состояние доски соответствует правильному - рисуем сообщение о победе
    if board == correct_board:
        # Эту функцию мы добавим позже
        show_victory_plate()


def get_inv_count():
    """Функция считающая количество перемещений"""
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i + 1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


def is_solvable():
    """Функция определяющая имеет ли головоломка рещение"""
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


#  Создаем список блоков
board = list(range(1, EMPTY_SQUARE + 1))
# Список с которым мы будем сравнивать результат. В данном случае это
# просто отсортированный список, но при желании можно придумать что-то другое
correct_board = board[:]
# перемешиваем блоки
while not is_solvable():
    shuffle(board)
# рисуем доску
draw_board()


canvas.pack()
root.mainloop()
