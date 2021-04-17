
def maths(one, func):
    if func is None:
        return one
    sym = func[0]
    two = func[1]
    if sym == '+':
        return one + two
    if sym == '-':
        return one - two
    if sym == '*':
        return one * two
    return one // two

def zero(func = None): 
    return maths(0,func)
def one(func = None):
    return maths(1,func)
def two(func = None):
    return maths(2,func)
def three(func = None):
    return maths(3,func)
def four(func = None):
    return maths(4,func)
def five(func = None):
    return maths(5,func)
def six(func = None):
    return maths(6,func)
def seven(func = None):
    return maths(7,func)
def eight(func = None):
    return maths(8,func)
def nine(func = None):
    return maths(9,func)

def plus(num):
    return ['+',num]
def minus(num):
    return ['-',num]
def times(num):
    return ['*',num]
def divided_by(num):
    return ['/',num]



seven(times(five()))
six(divided_by(two()))
three(minus(six()))
zero()

