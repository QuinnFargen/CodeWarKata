
Game = [ 
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]

def who_is_winner(Game):
    A = ["0"]*6;B = ["0"]*6;C = ["0"]*6;D = ["0"]*6;
    E = ["0"]*6;F = ["0"]*6;G = ["0"]*6      
    a,b,c,d,e,f,g = 0,0,0,0,0,0,0

    def whowins(Pieces):
        if "RRRR" in Pieces:
            return "Red"
        if "YYYY" in Pieces:
            return "Yellow"
        pass

    for i in range(len(Game)):
        if Game[i][0] == "A":
            A[a] = Game[i][2]
            a += 1
        if Game[i][0] == "B":
            B[b] = Game[i][2]
            b += 1
        if Game[i][0] == "C":
            C[c] = Game[i][2]
            c += 1
        if Game[i][0] == "D":
            D[d] = Game[i][2]
            d += 1
        if Game[i][0] == "E":
            E[e] = Game[i][2]
            e += 1
        if Game[i][0] == "F":
            F[f] = Game[i][2]
            f += 1
        if Game[i][0] == "G":
            G[g] = Game[i][2]
            g += 1
        # Row winners
        for i in range(6):
            row = A[i]+B[i]+C[i]+D[i]+E[i]+F[i]+G[i]
            #print(row)
            if whowins(row) is not None: 
                return whowins(row)
    
        # Col winners
        for i in [A,B,C,D,E,F,G]:
            col = ''.join(i)
            #print(col)
            if whowins(col) is not None: 
                return whowins(col)

        # Diag winners
        D1 = D[0] + E[1] + F[2] + G[3]
        D2 = C[0] + D[1] + E[2] + F[3] + G[4]
        D3 = B[0] + C[1] + D[2] + E[3] + F[4] + G[5]
        D4 = A[0] + B[1] + C[2] + D[3] + E[4] + F[5]
        D5 = A[1] + B[2] + C[3] + D[4] + E[5]
        D6 = A[2] + B[3] + C[4] + D[5]

        D7  = D[0] + C[1] + B[2] + A[3]
        D8  = E[0] + D[1] + C[2] + B[3] + A[4]
        D9  = F[0] + E[1] + D[2] + C[3] + B[4] + A[5]
        D10 = G[0] + F[1] + E[2] + D[3] + C[4] + B[5]
        D11 = G[1] + F[2] + E[3] + D[4] + C[5]
        D12 = G[2] + F[3] + E[4] + D[5]

        for i in [D1,D2,D3,D4,D4,D5,D6,D7,D8,D9,D10,D11,D12]:
            if whowins(i) is not None:
                return whowins(i)
    return "Draw"

who_is_winner(Game)

who_is_winner(Game)

Game[0][2]

A = list();B = list()
A += "c"
A,B
A[5] = 'Poop'
A = [0]*6
''.join(A)
a = ['a', 'b', 'c', 'd']
''.join(a)
str(A)
for i in range(5):
    print(i)

        a,b,c,d,e,f,g = 0,0,0,0,0,0,0

for i in [A,A,A,A,A]:
    print(i)      


    def winner(Pieces):
        if "RRRR" in Pieces:
            return "Red"
        if "YYYY" in Pieces:
            return "Yellow"
        pass

winner("YYYYYYY").__class__
winner("yy").__class__

if winner("YYYYYY") is not None:
    return winner("YYYYYY")

def who_is_winner(Game):
    
    #Define Board
    A = ["0"]*6;B = ["0"]*6;C = ["0"]*6;D = ["0"]*6;
    E = ["0"]*6;F = ["0"]*6;G = ["0"]*6      
    a,b,c,d,e,f,g = 0,0,0,0,0,0,0
    
    #Function used to see if winner present in Rows, Cols, & Diags
    def whowins(Pieces):
        if "RRRR" in Pieces:
            return "Red"
        if "YYYY" in Pieces:
            return "Yellow"
        pass
    
    # Loop through each piece played. Checking winners after each.
    for i in range(len(Game)):
        if Game[i][0] == "A":
            A[a] = Game[i][2]
            a += 1
        if Game[i][0] == "B":
            B[b] = Game[i][2]
            b += 1
        if Game[i][0] == "C":
            C[c] = Game[i][2]
            c += 1
        if Game[i][0] == "D":
            D[d] = Game[i][2]
            d += 1
        if Game[i][0] == "E":
            E[e] = Game[i][2]
            e += 1
        if Game[i][0] == "F":
            F[f] = Game[i][2]
            f += 1
        if Game[i][0] == "G":
            G[g] = Game[i][2]
            g += 1
            
            # Row winners
        for i in range(6):
            row = A[i]+B[i]+C[i]+D[i]+E[i]+F[i]+G[i]
            #print(row)
            if whowins(row) is not None: 
                return whowins(row)
    
            # Col winners
        for i in [A,B,C,D,E,F,G]:
            col = ''.join(i)
            #print(col)
            if whowins(col) is not None: 
                return whowins(col)

            # Diag winners
        D1 = D[0] + E[1] + F[2] + G[3]
        D2 = C[0] + D[1] + E[2] + F[3] + G[4]
        D3 = B[0] + C[1] + D[2] + E[3] + F[4] + G[5]
        D4 = A[0] + B[1] + C[2] + D[3] + E[4] + F[5]
        D5 = A[1] + B[2] + C[3] + D[4] + E[5]
        D6 = A[2] + B[3] + C[4] + D[5]

        D7  = D[0] + C[1] + B[2] + A[3]
        D8  = E[0] + D[1] + C[2] + B[3] + A[4]
        D9  = F[0] + E[1] + D[2] + C[3] + B[4] + A[5]
        D10 = G[0] + F[1] + E[2] + D[3] + C[4] + B[5]
        D11 = G[1] + F[2] + E[3] + D[4] + C[5]
        D12 = G[2] + F[3] + E[4] + D[5]

        for i in [D1,D2,D3,D4,D4,D5,D6,D7,D8,D9,D10,D11,D12]:
            if whowins(i) is not None:
                return whowins(i)
        
        # If every piece played and no winner, then it's a Draw.           
    return "Draw"          