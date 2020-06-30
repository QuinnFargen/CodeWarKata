
from itertools import permutations

def highest(n):
    nums = [int(d) for d in str(n)]
    # Permutations
    output = sum([list(map(list, permutations(nums, i))) for i in range(len(nums) + 1)], [])
    # Correct Size
    outsize = [i for i in output if len(i) == len(nums)]
    # Change to Ints
    numbers = [int(''.join(map(str, i))) for i in outsize]
    # Ints < n
    numlow = [i for i in numbers if i < n]
    if numlow == []:
        return -1
    else:
        return max(numlow)

def next_smaller(n):
    if isinstance(n, int):
        if len(str(n)) > 4:
            last4 = highest(int(str(n)[-4:]))
            if last4 == -1:
                return -1
            else:
                return int(str(n)[:-4] + str(last4))
        elif n < 21:
            return -1
        elif len(str(n)) <= 4:
            return highest(n)
    else:
        return -1



n = 43365644
n = 123456789
n = 'Quinn'
n = 907
n = 123456798
n = 1234567908
str(n)[-4:]
str(n)[:-4]

next_smaller(n)

next_smaller(907)
next_smaller(531)
next_smaller(135)
next_smaller(2071)
next_smaller(10)
next_smaller(123456798)
next_smaller(123456789)
next_smaller(1234567908)



# Test.it("Smaller numbers")
# Test.assert_equals(next_smaller(907), 790)
# Test.assert_equals(next_smaller(531), 513)
# Test.assert_equals(next_smaller(135), -1)
# Test.assert_equals(next_smaller(2071), 2017)
# Test.assert_equals(next_smaller(414), 144)
# Test.assert_equals(next_smaller(123456798), 123456789)
# Test.assert_equals(next_smaller(123456789), -1)
# Test.assert_equals(next_smaller(1234567908), 1234567890)