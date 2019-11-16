# import only system from os
from os import system, name

class Scanner:
    # define our clear function
    def clear(self):

        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def scan(self):
        result = ""
        print("Tamaño de matriz:")
        matrix_size = int(input())
        print()
        print("Ingresa la matriz por renglón y separa cada numero por una coma.")

        matrix=""
        for row in range(matrix_size):
            print("Renglón "+str(row)+": ")
            matrix += input()+"-"

        rows = matrix.split('-')

        G = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
        for i,row in enumerate(rows):
            if row != "":
                elements=row.split(',')
                for j,element in enumerate(elements):
                    G[i][j]=int(element)
        return G


