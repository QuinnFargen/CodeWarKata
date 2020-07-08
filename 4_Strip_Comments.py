
string = 'apples, pears # and bananas\ngrapes\nbananas !apples'
markers = ["#", "!"]

def solution(string,markers):
    spl = string.split('\n')
    for m in markers:
        spl = [i.split(m, 1)[0].rstrip() for i in spl] 
    return '\n'.join(spl)


import re
rtn = re.split('([.!?] *)', test2)
''.join([each.capitalize() for each in rtn])

test2=("The neighbour's ceiling fell on his head. the weight of it crushed him to the ground.")

Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")