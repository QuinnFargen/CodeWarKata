
board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

badboard = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 4, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

import numpy as np

def valid_solution(board):
    correct = [1,2,3,4,5,6,7,8,9]
    bored = np.array(board)
    #rows
    for i in list(range(0,9)):
        if not all(elem in bored[i]  for elem in correct):
            return False
    #cols
    bored_T = bored.T
    for i in list(range(0,9)):
        if not all(elem in bored_T[i]  for elem in correct):
            return False
    #cubes
    cubes = [[0,3,0,3], [0,3,3,6], [0,3,6,9],
             [3,6,0,3], [3,6,3,6], [3,6,6,9],
             [6,9,0,3], [6,9,3,6], [6,9,6,9]]
    for i in list(range(0,9)):
        n = cubes[i][0]; m = cubes[i][1]; a = cubes[i][2]; b = cubes[i][3]; 
        tempbored = [item for sublist in bored[n:m,a:b].tolist() for item in sublist]
        if not all(elem in tempbored  for elem in correct):
            return False
    #Else Board Good
    return True

valid_solution(board)
valid_solution(badboard)




try:
    valid_solution = validSolution
except NameError:
    pass

test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);