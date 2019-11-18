from Scanner import Scanner
from Matching import Matching



# matrix = [
#     [6, 10, 15, 0, 0],
#     [8, 0, 9, 4, 0],
#     [0, 7, 3, 11, 0],
#     [9, 5, 0, 3, 0],
#     [10,11,7,11,0],
# ]
# matrix = [
#     [6,10,15,0,4],
#     [8,0,9,4,5],
#     [0,7,3,11,9],
#     [9,5,0,3,8],
#     [10,11,7,11,0],
# ]
# matrix = [
#     [6,10,0,0,4],
#     [8,100,9,4,5],
#     [0,7,3,11,9],
#     [9,5,0,3,8],
#     [10,11,7,11,0],
# ]
# matrix = [
#     [6, 8, 0],
#     [8, 6, 0],
#     [8, 6, 0],
# ]

# matrix = [
#     [80, 40, 50, 46],
#     [40, 70, 20, 25],
#     [30, 10, 20, 30],
#     [35, 20, 25, 30],
# ]

# matrix = [
#     [1, 2, 8, 0, 3],
#     [4, 9, 7, 5, 0],
#     [2, 0, 10, 0, 8],
#     [6, 3, 0, 9, 4],
#     [0, 8, 0, 7, 9]
# ]

matrix = [
    [0, 2, 8, 0, 0],
    [0, 9, 7, 0, 0],
    [0, 0, 0, 0, 8],
    [0, 0, 0, 9, 4],
    [0, 0, 0, 0, 0]
]

test = Matching(matrix, len(matrix))
test.algorithm()
print("Matriz:")
for row in matrix:
    print(row)
print("Cost: ", test.get_cost())
print("Matching: ", test.get_match())


#
# flg_stop=False
# while not flg_stop:
#     scan = Scanner()
#     matrix=None
#     test=None
#     matrix=scan.scan()
#     test = Matching(matrix, len(matrix))
#     test.algorithm()
#     scan.clear()
#     print("Matriz:")
#     for row in matrix:
#         print(row)
#     print("Cost: ", test.get_cost())
#     print("Matching: ", test.get_match())
#     print()
#     print("¿Quieres ingresar otra matriz? Y/N")
#     if input().upper()=="N":
#         flg_stop=True
