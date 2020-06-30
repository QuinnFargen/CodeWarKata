data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
range(len(data1) % 8)
int(len(data1) / 8)
data1[-8:]
del data1[-8:]
data1

def datareverse(data):
    new = list()
    for i in range(int(len(data) / 8)):
        new.extend(data[-8:])
        del data[-8:]
        #print(new);print(data)
    return new

            
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
this = datareverse(data1)
this















