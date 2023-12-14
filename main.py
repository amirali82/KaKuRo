from DataStruct import GameData
from ui import draw_grid
from Solver import solve_kauro

index = input("Input test number(from 1 to 4):")
index = int(index)

if (1 <= index and index <= 4):
    x = GameData("./kakuro data/test" + str(index) + ".txt")
    solve_kauro(x)
    draw_grid(x)
else:
    print("Input should be a number between 1 and 4. Run the program again.")

