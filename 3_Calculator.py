
import operator

class Calculator(object):
    # Possible operations
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}

    # evaluate function used in test
    def evaluate(self, string):
        self.result = string.split(' ')
        # Loop through multi/divide then add/minus
        self._loop('*/')
        self._loop('+-')
        return float(self.result[0])

    def _loop(self, operations):
        i = 1
        while i < len(self.result) - 1:
            if self.result[i] in operations:
                #replace prior spot (first of operation in loop)
                self.result[i - 1] = str(self.__class__.operations[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                #remove operation and following value used in operation
                self.result.pop(i + 1)
                self.result.pop(i)
                continue
            i += 1

    

string = '2 / 2 + 3 * 4 - 6'
string.split(' ')

str(self.__class__.operands[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))


Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7