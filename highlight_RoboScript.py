
# F - Wrap this command around <span style="color: pink"> and </span> 
# L - Wrap this command around <span style="color: red"> and </span> ]
# R - Wrap this command around <span style="color: green"> and </span> 
# Digits from 0 through 9 - Wrap these around <span style="color: orange"> and </span> tags so that they are highlighted orange in our editor

code = 'F3RF5LF7'
code = 'FFFR345F2LL'


from itertools import groupby
def highlight(code):
    beg = '<span style="color: '; mid = '">'; end = '</span>'
    F = 'pink'; L = 'red'; R = 'green'; num = 'orange'
    code_grpnum = [''.join(g) for k, g in groupby(code, lambda x: x.isdigit())]
    
    codegrp = [''.join(g) for k, g in groupby(code)]
    finalstr = ''
    for i in codegrp:
        if 'F' in i:
            color = F
        elif 'L' in i:
            color = L
        elif 'R' in i:
            color = R
        elif i.isdigit():
            color = num        
        finalstr += beg + color + mid + i + end
    return finalstr

codelist[- 1] is '7'

from itertools import groupby

[''.join(g) for k, g in groupby(code)]
code_grpnum = [''.join(g) for k, g in groupby(code, lambda x: x.isdigit())]
for n, i in enumerate(code_grpnum):
    i = 'FFFR';n = 0
    if not i.isdigit():
        temp_insert = [''.join(g) for k, g in groupby(i)]
        if temp_insert != []:
            code_final = code_grpnum.pop(n)
            for i in temp_insert:
                i = 'FFF'
                i = 'R'
                code_grpnum.insert(n, i)

[item for sublist in code_grpnum  for item in sublist]

[''.join(g) for k, g in groupby(code_grpnum)]


highlight("F3RF5LF7")
# "<span style=\"color: pink\">F</span>
# <span style=\"color: orange\">3</span>
# <span style=\"color: green\">R</span>
# <span style=\"color: pink\">F</span>
# <span style=\"color: orange\">5</span>
# <span style=\"color: red\">L</span>
# <span style=\"color: pink\">F</span>
# <span style=\"color: orange\">7</span>"

# <span style="color: pink">F</span>
# <span style="color: orange">3</span>
# <span style="color: green">R</span>
# <span style="color: pink">F</span>
# <span style="color: orange">5</span>
# <span style="color: red">L</span>
# <span style="color: pink">F</span>
# <span style="color: orange">7</span>


l = list(range(3))
print(l)
# [0, 1, 2]

l.insert(0, 100)
print(l)
# [100, 0, 1, 2]

l.insert(0, 200)
print(l)