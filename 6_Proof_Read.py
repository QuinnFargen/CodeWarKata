#Proof Read

"""
You've just finished writing the last chapter for your novel when a virus suddenly infects your document. It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters. Write a function which will:

a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine, deceive, weight)

b) only capitalise the first letter of each sentence. Make sure the rest of the sentence is in lower case.
"""


"""
"He haD iEght ShOTs of CAffIEne"
"He had eight shots of caffeine"
"""


def proofread(string):
    import re
    rtn = string.lower().replace("ie","ei").capitalize()
    rtn2 = re.split('([.!?] *)', rtn)
    return ''.join([each.capitalize() for each in rtn2])

proofread(test2)

"The neighbour's ceiling fell on his head. the weight of it crushed him to the ground."
"The neighbour's ceiling fell on his head. The weight of it crushed him to the ground."

test = "He haD iEght ShOTs of CAffIEne"
test.capitalize()
test.lower().find("ie")
test.find("iE")

testlow = test.lower()
testlow[7] = "e"

import re
rtn = re.split('([.!?] *)', test2)
''.join([each.capitalize() for each in rtn])

test2=("The neighbour's ceiling fell on his head. the weight of it crushed him to the ground.")
sentence='.'.join([i.capitalize() for i in test2.split('.')])
print(sentence)