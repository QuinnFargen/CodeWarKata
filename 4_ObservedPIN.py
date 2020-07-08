"""

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw 
could actually be another adjacent digit (horizontally or vertically, but not diagonally). 
E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be 
the 2, 4, 6 or 8.

"""

observed = '369'

from itertools import product

def get_pins(observed):
    pad = [ ['0','8'], ['1','2','4'], ['2','1','3','5'], ['3','2','6']
                , ['4','1','5','7'], ['5','2','4','6','8'], ['6','3','5','9']
                , ['7','4','8'], ['8','5','7','9','0'], ['9','6','8']]
    pin = [int(i) for i in list(observed)]
    poss = [pad[i] for i in pin]
    return [''.join(s) for s in product(*poss)]



get_pins('11')





test.describe('example tests')
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

