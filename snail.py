
import pandas as pd


snail_map = [[1,2,3],
         [4,5,6],
         [7,8,9]]

snail = pd.DataFrame(snail_map)

expected = [1,2,3,6,9,8,7,4,5]

def snail(snail_map):
    n = len(snail_map[0])
    m = len(snail_map)
    snail_order = []
  
    #First row
    toprow = 0  
    snail_order.extend(snail_map[toprow][0:n])
    #Right col down
    snail_order.append(snail_map[1][m-1])
    #Reverse last row
    snail_map[n-1].reverse()
    snail_order.extend(snail_map[n-1])
    #Left col up
    snail_order.append(snail_map[1][0])

reverse([1,2,3])