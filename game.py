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


canvas.pack()
draw_board()
root.mainloop()
