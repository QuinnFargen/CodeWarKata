



def persistence(num):
    count = 0
    print(num)
    while len(str(num)) > 1:
        number = [int(d) for d in str(num)]
        mult = 1
        for x in number:
            mult *= x
            num = mult
        count += 1
        #print(num)
        #print(mult)
        #print(count)
        #print(number)
        #print(len(str(num)))
    return count 
    
persistence(39)

len(str(594))

str(594)[1]

number = [int(d) for d in str(394)]
number[1:len(number)]

4*4*3*2
9*6
5*4
2*0

39 * 3 * 9