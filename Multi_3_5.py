# Finish the solution so that it returns the sum of all the 
# multiples of 3 or 5 below the number passed in.


def solution(number):
    numlist = list(range(1, number))
    numlist_35 = [ x for x in numlist if x % 5 == 0 or x % 3 == 0 ]
    return sum(numlist_35)

solution(33)

num = 33

numlist = list(range(1, num))
numlist_35 = [ x for x in numlist if x % 5 == 0 or x % 3 == 0 ]
sum(numlist_35)

18 % 3


