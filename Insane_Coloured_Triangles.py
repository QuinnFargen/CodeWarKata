

# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G

colours = 'RRR'
colours = 'RBRGBRBGGRRRBGBBBGG'
row = 'RBRGBRBGGRRRBGBBBGG'
row = 'RBRGBRB'


len(row*100)
rowlong = row*100
rowmid = row*10


colours = set("RGB")

def triangle(row):
    while len(row)>1:
        row = ''.join( F if F == S else (colours - {F,S}).pop() for F,S in zip(row, row[1:]) )
        print(row)
    return row

triangle(row)
triangle(rowmid)
triangle(rowlong)

GGB            BRG
GRGBGBBRGRBBRGBGB
BBRRRBGBBGBGBRRR
BGRRGRRBRRRRGRR
RBRBBRGGRRRBBR
GGGBGBGBRRGBG
GGRRRRRGRBRR
GBRRRRBBGGR
RGRRRGBRGB
BBRRBRGBR
BGRGGBRG
RBBGRGB
GBRBBR
RGGBG
BGRR
RBR
GG
G

R B R G B R B G G R R R B G B B B G G

R B R G B R G G R B G B G
G G B R G B G B G R R R
G R G B R B R
B B R G G G
B R G
G B
R

G