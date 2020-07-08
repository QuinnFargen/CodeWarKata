
import numpy as np

def done_or_not(board):
    correct = [1,2,3,4,5,6,7,8,9]
    bored = np.array(board)
    #rows
    for i in list(range(0,9)):
        if not all(elem in bored[i]  for elem in correct):
            return 'Try again!'
    #cols
    bored_T = bored.T
    for i in list(range(0,9)):
        if not all(elem in bored_T[i]  for elem in correct):
            return 'Try again!'
    #cubes
    cubes = [[0,3,0,3], [0,3,3,6], [0,3,6,9],
             [3,6,0,3], [3,6,3,6], [3,6,6,9],
             [6,9,0,3], [6,9,3,6], [6,9,6,9]]
    for i in list(range(0,9)):
        n = cubes[i][0]; m = cubes[i][1]; a = cubes[i][2]; b = cubes[i][3]; 
        tempbored = [item for sublist in bored[n:m,a:b].tolist() for item in sublist]
        if not all(elem in tempbored  for elem in correct):
            return 'Try again!'
    #Else Board Good
    return 'Finished!'

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

badboard = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
            ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
            ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
            ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
            ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
            ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
            ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
            ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
            ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]

done_or_not(board)
done_or_not(badboard)



  test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
                        
test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');