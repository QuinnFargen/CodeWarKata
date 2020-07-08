
string = 'aabb'

import itertools 

def permutations(string):
    perms = list(itertools.permutations(list(string)))
    dupl = [''.join(i) for i in perms]
    return list(set(dupl))




Test.assert_equals(sorted(permutations('a')), ['a']);
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])