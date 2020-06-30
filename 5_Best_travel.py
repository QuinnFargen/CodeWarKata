

from itertools import combinations 

ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
k = 4
t = 230
comb = list(combinations(ls, k))
list1 = [ elem for elem in comb if sum(elem) <= t]
sum(max(list1))
sum(list1)
list1[0:5]
[sum(i) for i in list1[0:5]]

from itertools import combinations 

def choose_best_sum(t, k, ls):
    comb = list(combinations(ls, k))
    comb_k = [ elem for elem in comb if sum(elem) <= t]
    sums = [sum(i) for i in comb_k]
    if comb_k == []:
        return None
    # return [sums,comb_k]
    return max(sums)

choose_best_sum(430,5,ls)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
Test.assert_equals(choose_best_sum(230, 4, xs), 230)
Test.assert_equals(choose_best_sum(430, 5, xs), 430)
Test.assert_equals(choose_best_sum(430, 8, xs), None)