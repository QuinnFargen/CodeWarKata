# return masked string
def maskify(cc):
    cc = str(cc)
    if len(cc) < 5:
        return cc
    else:    
        R4 = cc[-4:]
        NumHash = len(cc) - 4
        return "#"*NumHash + R4