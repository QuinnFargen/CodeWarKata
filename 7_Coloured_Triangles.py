
# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G

colours = 'RRR'
colours = 'RBRGBRBGGRRRBGBBBGG'
row = 'RBRGBRBGGRRRBGBBBGG'
row = 'RBRGBRB'

def whichcolor(F,S):
    if F == S:
        return F    #Same just use the first
    elif 'R' not in F+S:
        return 'R'
    elif 'G' not in F+S:
        return 'G'
    elif 'B' not in F+S:
        return 'B'

def triangle(row):
    colours = list(row)
    N_Col = []
    while len(colours) > 1:
        for i in range(len(colours) - 1):
            N_Col += whichcolor(colours[i], colours[i + 1])        
        colours = list(N_Col)
        print(colours)
        N_Col = []    
    return colours[0]



from itertools import groupby
[''.join(g) for k, g in groupby(colours)]


R R R R R G B B
R R R R B R B
R R R G G G
R R B G G
R G R G
B B B


B

R R R R G G G G B B B B
R R R B G G G R B B B
R R G R G G B G B B
R B B B G R R R B
G B B R B R R G
R B G G G R B
G R G G B G
B B G R R
B R B R
G G G
G G
G

R R R R G G G G B B B B
R R R B 
R R G R 
R B B B


R G B
B R
G


R R G B R G B B
R B R G B R B
G G B R G G
G R G B G
B B R R
B G R
R B
G


test.assert_equals(triangle('GB'), 'R')
test.assert_equals(triangle('RRR'), 'R')
test.assert_equals(triangle('RGBG'), 'B')
test.assert_equals(triangle('RBRGBRB'), 'G')
test.assert_equals(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
test.assert_equals(triangle('B'), 'B')