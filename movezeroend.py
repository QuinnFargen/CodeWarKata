
array = ["a",0,0,"b",None,"c","d",0,1,False,0,1,True,0,3,[],0,1,9,0,0,{},0,0,9] #),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
array = [1,2,0,1,0,1,0,3,0,1]

def move_zeros(array):
    if array == []:
        return array
    # if array[-1] == 0:
    #     array = array[0:-1]
    num0 = array.count(0)
    array = list(filter(lambda a: a == 0 & isinstance(a, bool), array))
    array.extend([0] * num0)
    return array

False != 0 & isinstance(False,int)
False == 0
True == 0
False != False
isinstance(True,bool)
isinstance(False,bool)

move_zeros(array)

test = [1, None, 2, 1, 0, 0, 0]
test.count(0)
test[-1]

num0 = test.count(0)
#remove zeros
test = list(filter(lambda a: a != 0, test))
#add zeros end
test.extend([0] * num0)


Test.describe("Basic tests")
Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
Test.assert_equals(move_zeros(["a","b"]),["a","b"])
Test.assert_equals(move_zeros(["a"]),["a"])
Test.assert_equals(move_zeros([0,0]),[0,0])
Test.assert_equals(move_zeros([0]),[0])
Test.assert_equals(move_zeros([False]),[False])
Test.assert_equals(move_zeros([]),[])