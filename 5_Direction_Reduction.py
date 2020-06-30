"""
Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" 
are opposite, "WEST" and "EAST" too. Going to one direction and coming back 
the opposite direction is a needless effort. Since this is the wild west, 
with dreadfull weather and not much water, it's important to save yourself some energy, 
otherwise you might die of thirst!

Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] 
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" 
are not directly opposite of each other and can't become such. 
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
"""


test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
[word.replace("NORTH","N").replace("SOUTH","S").replace("EAST","E").replace("WEST","W") for word in test]


def dirReduc(arr):
    arr = [word.replace("NORTH","N").replace("SOUTH","S").replace("EAST","E").replace("WEST","W") for word in arr]
    loop = True
    while loop == True:
        initial = len(arr)
        for i in range(len(arr)-1):
            if (arr[i] == "N" and arr[i+1] == "S") or (arr[i] == "S" and arr[i+1] == "N"):
                del arr[i];del arr[i];break
        if len(arr) == initial:
            for i in range(len(arr)-1):   
                if (arr[i] == "E" and arr[i+1] == "W") or (arr[i] == "W" and arr[i+1] == "E"):
                    del arr[i];del arr[i];break
            if len(arr) == initial:
                loop = False
        else:
            loop = True

    return [word.replace("N","NORTH").replace("S","SOUTH").replace("E","EAST").replace("W","WEST") for word in arr]
   



dirReduc(test)

del test[1];del test[1]

test2 = [word.replace("NORTH","N").replace("SOUTH","S").replace("EAST","E").replace("WEST","W") for word in test]
test2

loop = True
while loop == True:
    initial = len(test2)
    for i in range(len(test2)-1):
        if (test2[i] == "N" and test2[i+1] == "S") or (test2[i] == "S" and test2[i+1] == "N"):
            del test2[i];del test2[i];break
    if len(test2) == initial:
        for i in range(len(test2)-1):   
            if (test2[i] == "E" and test2[i+1] == "W") or (test2[i] == "W" and test2[i+1] == "E"):
                del test2[i];del test2[i];break
        if len(test2) == initial:
            loop = False
    else:
        loop = True

test2