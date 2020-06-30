

Task
Your MyRobot-specific (esoteric) scripting language called RoboScript only ever contains the following characters: F, L, R, the digits 0-9 and brackets (( and )). Your goal is to write a function highlight which accepts 1 required argument code which is the RoboScript program passed in as a string and returns the script with syntax highlighting. The following commands/characters should have the following colors:

F - Wrap this command around <span style="color: pink"> and </span> tags so that it is highlighted pink in our editor
L - Wrap this command around <span style="color: red"> and </span> tags so that it is highlighted red in our editor
R - Wrap this command around <span style="color: green"> and </span> tags so that it is highlighted green in our editor
Digits from 0 through 9 - Wrap these around <span style="color: orange"> and </span> tags so that they are highlighted orange in our editor
Round Brackets - Do not apply any syntax highlighting to these characters
For example:

highlight("F3RF5LF7"); // => 
    "
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">3</span>
    <span style=\"color: green\">R</span>
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">5</span>
    <span style=\"color: red\">L</span>
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">7</span>
    "
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">3</span>
    <span style=\"color: green\">R</span>
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">5</span>
    <span style=\"color: red\">L</span>
    <span style=\"color: pink\">F</span>
    <span style=\"color: orange\">7</span>


    '<span style="color: pink">F</span>
    <span style="color: pink">F</span>
    <span style="color: pink">F</span>
    <span style="color: green">R</span>
    <span style="color: orange">3</span>
    <span style="color: orange">4</span>
    <span style="color: orange">5</span>
    <span style="color: pink">F</span>
    <span style="color: orange">2</span>
    <span style="color: red">L</span>
    <span style="color: red">L</span>' 
    
should equal 
    '<span style="color: pink">FFF</span>
    <span style="color: green">R</span>
    <span style="color: orange">345</span>
    <span style="color: pink">F</span>
    <span style="color: orange">2</span>
    <span style="color: red">LL</span>'






def highlight(code):    
        # Stuff used below for loops and strings
    beg = '<span style="color: '
    mid = '">'
    end = '</span>'
    combine = ''
    value = ''
    extra = 0

    # Turn string into the unique types
    clean = test.replace("0","N").replace("1","N").replace("2","N").replace("3","N").replace("4","N").replace("5","N").replace("6","N").replace("7","N").replace("8","N").replace("9","N")
    clean = clean.replace("(","P").replace(")","P")
    

    for i in range(len(code) -1):
        j = True    #Set / Reset
        plus = 0    #Set / Reset 
        if i < extra:
            continue    # if just inserted more than one, than loop till new value

    #Parenthesis
        if clean[i] == 'P':
            #Need to pass through the Parenthesis
            ###################################
            #Check how many have the same value
            while j == True:
                if clean[i] == clean[i+plus]:
                    value = clean[i:(i+plus)]
                    value = code[i:i+plus]    #Set Actual String values
                    plus +=1; extra +=1
                else:
                    value = code[i]
                    j = False
            ###################################
            
    #Numbers
        elif clean[i] == 'N':
            color = 'orange'
            ###################################
            #Check how many have the same value
            while j == True:
                if clean[i] == clean[i+plus]:
                    value = code[i:i+plus]    #Set Actual String values
                    plus +=1; extra +=1
                else:
                    value = code[i]
                    j = False
            ###################################
    #Letters
        elif clean[i] == 'F':
            color = 'pink'
            ###################################
            #Check how many have the same value
            while j == True:
                if clean[i] == clean[i+plus]:
                    value = code[i:i+plus]    #Set Actual String values
                    plus +=1; extra +=1
                else:
                    value = code[i]
                    j = False
            ###################################

        elif clean[i] == 'L':
            color = 'red'
            ###################################
            #Check how many have the same value
            while j == True:
                if clean[i] == clean[i+plus]:
                    value = code[i:i+plus]    #Set Actual String values
                    plus +=1; extra +=1
                else:
                    value = code[i]
                    j = False
            ###################################

        elif clean[i] == 'R':
            color = 'green'

            ###################################
            #Check how many have the same value
            while j == True:
                if clean[i] == clean[i+plus]:
                    value = code[i:i+plus]    #Set Actual String values
                    plus +=1; extra +=1
                else:
                    value = code[i]
                    j = False
            ###################################
        print(value)
        combine += beg + color + mid + value + end

    return combine


highlight("FFLR2543LFFF")




test = 'FFLRNNNNLPPFFF'


dupl = list()

for i in range(len(test)-1):
    plus = 1; j = True
    print("For " + str(i) + ":")
    print("-------------------")
    while j == True:
        #Plus has reached max
        if (i+plus) >= len(test):
            plus -= 1
            j = False
            print("if")
        #Next equals current
        elif test[i] == test[i+plus]:
            value = test[i:i+plus]
            print(test[i:plus + i])
            plus +=1
            print("elif 1")
        #Next Not Equal Current but did previous
        elif test[i] != test[i+plus] and plus > 0:
            j = False 
            print("elif 2")
        #Next Not Equal To Current and no previous
        else:
            value = test[i]
            j = False
            print("else")
        print("Value:    " + str(value))
        print("String:   " + str(test[i]))
        print("String+i: " + str(test[plus + i]))
        print("Plus:     " + str(plus))
        print("Plus+1:   " + str(test[i:plus + i]))
        print("------")

    print(value)
    dupl += value


this = list()
this += 'Fart'


for i in range(len(test)-1):
    plus = 0; j = True
    while j == True:
        print(i)
        print(plus)
        print(i+plus)
        if (i+plus) >= len(test):
            j = False
        elif test[i] == test[i+plus]:
            plus +=1
            if (i+plus) > len(test):
                j = False
        elif test[i] == test[i+plus] and plus > 0:
            j = False 
        else:
            j = False

len(test)

test = 'FFLR2543L))FFF'
dupl = list()
for i in range(len(test) - 1):
    end = i; j = True
    while j == True:
       if test[i] == test[i+end]:
           end += 1
       else:
            j = False
    print(test[i:end])        
    dupl += test[i:end]
    print(dupl)
        
test.replace("1","N").replace("2","N").replace("3","N").replace("4","N").replace("5","N").replace("6","N").replace("7","N").replace("8","N").replace("9","N").replace("(","P").replace(")","P")

test = 'FFLR2543LFFF'
dupl = list()
j = 1
for i in range(len(test) - 1):
    if i < j:
        # Check how many equal current
        k = True
        start = i
        while k == True:
            if test[i] == test[start+1]:
                start += 1
                j += 1
            else: 
                k = False
                j += 1

    dupl += test[i:(start+1)]
    print(test[i:(start+1)])
    print(dupl)



test[1:4]


test.isdigit()
test[4].isdigit()

for i in range(len(test) - 1):
    print(i)

