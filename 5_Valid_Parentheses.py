


# (())((()())())
# "hi(hi)()"

bad = ')('
this = 'hi(hi)()'
this2 = '(())(((Quinn)())())'


# Need to find spots of closed () and mark the first ( so then I can loop thru and remove all pairs like this

def valid_parentheses(string):
    if len(string) == 0:
        return True
    s = ''.join(c for c in string if c in set('()'))
    pair = s.find('()')
    while pair != -1:
        s = s[:pair] + s[(pair + 2):]
        if len(s) == 0:
            break
        pair = s.find('()')
    if pair == -1:
        return False
    return True

valid_parentheses(this2)

def valid_parentheses(string):
    if len(string) == 0:
        return True
    s = ''.join(c for c in string if c in set('()'))
    while s.find('()') != -1:
        s = s[:s.find('()')] + s[(s.find('()') + 2):]
        if len(s) == 0:
            return True
    return False


# All below is wack code :)


def firstlastpars(str):
    if str[0] == '(' and str[-1] == ')':
        return str[1:-1]
    else:
        return -1

def valid_parentheses(string):
    pars = onlypars(string)
    while len(pars) > 0:
        pars = firstlastpars(pars)
        if pars == '':
            return True
        elif pars == -1:
            return False

expr = 'hi(hi)()'
def valid_parentheses(string):
    expr = onlypars(expr)
    stack = []
    for char in expr: 
        if char in ["("]: 
            stack.append(char) 
        else:  
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
        if stack: 
            return False
        return True

stacks(expr)

test = 'asfjas;dfl'
len('')

valid_parentheses('hi(hi)()')


Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)