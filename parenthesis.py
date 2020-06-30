

def onlypars(str):
    want = set('()')
    return ''.join(c for c in str if c in want)

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