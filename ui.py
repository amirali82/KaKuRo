import tkinter as tk
from tkinter import font as tkFont

CELL_SIZE = 50


def draw_grid(data):
    n = data.n
    m = data.m

    root = tk.Tk()
    root.title("KaKuRo")
    canvas = tk.Canvas(root, width=m*CELL_SIZE, height=n*CELL_SIZE)
    canvas.pack()

    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=10)

    for i in range(n):
        for j in range(m):
            x1 = i * CELL_SIZE
            y1 = j * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if (data.isVarible[i][j]):
                canvas.create_rectangle(y1, x1, y2, x2, fill="white", outline="black")
                canvas.create_text(
                    (y2 + y1) / 2,  (x2 + x1) / 2 
                , text=data.value[i][j], fill="black", font=("Arial", 20)) 
            elif (data.UData[i][j] == -1 and data.LData[i][j] == -1):
                canvas.create_rectangle(y1, x1, y2, x2, fill="black", outline="white")
            else:
                canvas.create_rectangle(y1, x1, y2, x2, fill="black", outline="white")
                canvas.create_line(y1, x1, y2, x2, fill="white")

                if (data.LData[i][j] != -1):
                    canvas.create_text(
                        (y2 - y1) / 4 + y1, 3 * (x2 - x1) / 4 + x1
                    , text=data.LData[i][j], fill="white")
                if (data.UData[i][j] != -1):
                    canvas.create_text(
                        3 * (y2 - y1) / 4 + y1, (x2 - x1) / 4 + x1
                    , text=data.UData[i][j], fill="white")

    root.mainloop()

