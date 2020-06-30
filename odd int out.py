test = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
len(test)
test[1:].index(20)

def find_it(test):
    numbers = test
    for i in range(len(test)):
        a = numbers[0]
        if a not in numbers[1:]:
            return a
        b = numbers[1:].index(a)
        del numbers[0]; del numbers[b]

test = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5,8,8]
find_it(test)
        


for i in range(len(test)):
    print(i)



quinn = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

del quinn[9]; del quinn[4]

quinn