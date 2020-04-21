def main():
    print("AORS-ИЛИ-НЕ - 1\nAORS-И-НЕ - 2\nCORS-И-НЕ - 3\nСДRS-И-НE - 4")
    print("CДJK-И-НЕ - 5\nCДD-И-НЕ - 6\nДD - 7")
    answer = '1'
    while (answer > '0' and answer < '8'):
        answer = input("What type? 1 - 8 : ")
        if answer == '1':
            first()
        elif answer == '2':
            second()
        elif answer == '3':
            third()
        elif answer == '4':
            fourth()
        elif answer == '5':
            fifth()
        elif answer == '6':
            sixth()
        elif answer == '7':
            seventh()
        else:
            print("Incorrect")
    return 0

def print_field(i):
    string = "0123456789"
    print(" " * (i + 10) + "1" * 10)
    print(" " * i + string * 2)

def reverse_sig(sig):
    if sig == '1':
        sig = '0'
    elif sig == '0':
        sig = '1'
    return sig

def getC():
    print_field(3)
    C = input("C: ")
    C_arr = []
    for i in C:
        C_arr.append(i)
    return C_arr

def getR():
    print_field(3)
    R = input("R: ")
    R_arr = []
    for i in R:
        R_arr.append(i)
    return R_arr

def getS():
    print_field(3)
    S = input("S: ")
    S_arr = []
    for i in S:
        S_arr.append(i)
    return S_arr

def getD():
    print_field(3)
    D = input("D: ")
    D_arr = []
    for i in D:
        D_arr.append(i)
    return D_arr

def getJ():
    print_field(3)
    J = input("J: ")
    J_arr = []
    for i in J:
        J_arr.append(i)
    return J_arr

def getK():
    print_field(3)
    K = input("K: ")
    K_arr = []
    for i in K:
        K_arr.append(i)
    return K_arr

# ! WORKS
def first():
    R = getR()
    S = getS()
    Q = [ 9 for i in range(len(R))]
    unQ = [ 9 for i in range(len(R))]
    danger = False
    for i in range(len(R)):
        if R[i] == '1' and S[i] == '0':
            #reset
            danger = False
            Q[i] = '0'
            unQ[i] = '1'
        elif R[i] == '0' and S[i] == '1':
            #set
            danger = False
            Q[i] = '1'
            unQ[i] = '0'
        elif R[i] == '1' and S[i] == '1':
            #danger
            danger = True
            Q[i] = '0'
            unQ[i] = '0'
        elif R[i] == '0' and S[i] == '0':
            #save
            if danger:
                Q[i] = 'X'
                unQ[i] = 'X'
            else:
                Q[i] = 'P'
                unQ[i] = 'P'
    cache = Q[0]
    for i in range(1, len(Q)):
        if Q[i] == 'P':
            Q[i] = cache
        cache = Q[i]
    
    cache = unQ[0]
    for i in range(1, len(unQ)):
        if unQ[i] == 'P':
            unQ[i] = cache
        cache = unQ[i]

    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

# ! WORKS
def second():
    R = getR()
    S = getS()
    Q = [ 9 for i in range(len(R))]
    unQ = [ 9 for i in range(len(R))]
    danger = False
    for i in range(len(R)):
        if R[i] == '1' and S[i] == '0':
            danger = False
            Q[i] = '0'
            unQ[i] = '1'
        elif R[i] == '0' and S[i] == '1':
            danger = False
            Q[i] = '1'
            unQ[i] = '0'
        elif R[i] == '0' and S[i] == '0':
            danger = True
            Q[i] = '1'
            unQ[i] = '1'
        elif R[i] == '1' and S[i] == '1':
            if danger:
                Q[i] = 'X'
                unQ[i] = 'X'
            else:
                Q[i] = 'P'
                unQ[i] = 'P'
    cache = Q[0]
    for i in range(1, len(Q)):
        if Q[i] == 'P':
            Q[i] = cache
        cache = Q[i]
    
    cache = unQ[0]
    for i in range(1, len(unQ)):
        if unQ[i] == 'P':
            unQ[i] = cache
        cache = unQ[i]

    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + unQ)
    print("U: " + Q)

# ! WORKS
def third():
    C = getC()
    R = getR()
    S = getS()
    Q = [ 9 for i in range(len(C))]
    unQ = [ 9 for i in range(len(C))]
    danger = False
    for i in range(len(R)):
        if C[i] == '1':
            if R[i] == '1' and S[i] == '0':
                danger = False
                Q[i] = '0'
                unQ[i] = '1'
            elif R[i] == '0' and S[i] == '1':
                danger = False
                Q[i] = '1'
                unQ[i] = '0'
            elif R[i] == '1' and S[i] == '1':
                danger = True
                Q[i] = '1'
                unQ[i] = '1'
            elif R[i] == '0' and S[i] == '0':
                if danger:
                    Q[i] = 'X'
                    unQ[i] = 'X'
                else:
                    Q[i] = 'P'
                    unQ[i] = 'P'
        if C[i] == '0':
            # save zone
            if danger:
                Q[i] = 'X'
                unQ[i] = 'X'
            else:
                Q[i] = 'P'
                unQ[i] = 'P'
    cache = Q[0]
    for i in range(1, len(Q)):
        if Q[i] == 'P':
            Q[i] = cache
        cache = Q[i]
    
    cache = unQ[0]
    for i in range(1, len(unQ)):
        if unQ[i] == 'P':
            unQ[i] = cache
        cache = unQ[i]

    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

# ! WORKS
def fourth():
    C = getC()
    R = getR()
    S = getS()
    Q = [ '9' for i in range(len(C))]
    unQ = [ '9' for i in range(len(C))]
    Q[0] = input("Input first of Q: ")
    if Q[0] == '0':
        unQ[0] = '1'
    else:
        unQ[0] = '0'
    state = ''
    cache = Q[0]
    for i in range(1, len(Q)):
        if C[i - 1] == '1' and C[i] == '0':
            if R[i - 1] == '1' and S[i - 1] == '1':
                Q[i] = reverse_sig(cache)
                cache = Q[i]
                state = Q[i]
            if R[i - 1] == '0' and S[i - 1] == '0':
                # Предыдущее состояние выбираем действие
                Q[i] = state
            if R[i - 1] == '1' and S[i - 1] == '0':
                Q[i] = '0'
                state = Q[i]
            if R[i - 1] == '0' and S[i - 1] == '1':
                Q[i] = '1'
                state = Q[i]
        else:
            #save zone
            Q[i] = Q[i - 1]
        

    # reverse
    for i in range(len(Q)):
        unQ[i] = reverse_sig(Q[i])
    
    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

# ! WORKS
def fifth():
    C = getC()
    J = getJ()
    K = getK()
    Q = [ 'N' for i in range(len(C))]
    unQ = [ 'N' for i in range(len(C))]
    print(len(Q))
    Q[0] = input("Input first of Q: ")
    cache = Q[0]
    for i in range(1, len(Q)):
        print(Q)
        if C[i - 1] == '1' and C[i] == '0':
            if J[i - 1] == '1' and K[i - 1] == '1':
                #print("reverse")
                # REVERSE
                Q[i] = reverse_sig(cache)
                cache = Q[i]
            if J[i - 1] == '1' and K[i - 1] == '0':
                #print("jerk")
                # JERK
                Q[i] = '1'
                cache = Q[i]
            if J[i - 1] == '0' and K[i - 1] == '1':
                #print("kill")
                # KILL
                Q[i] = '0'
                cache = Q[i]
            if J[i - 1] == '0' and K[i - 1] == '0':
                # SAVE
                if J[i - 2] == '1' and K[i - 2] == '1':
                    #print("reverse")
                    #print("NOW CACHE IS " + cache)
                    #print("NOW Q[i] IS " + Q[i])
                    Q[i] = reverse_sig(cache)
                    #print("NOW Q[i] IS " + Q[i])
                    
                    cache = Q[i]
                    #print("RRRNOW CACHE IS " + cache)
                if J[i - 2] == '1' and K[i - 2] == '0':
                    # JERK
                    #print("jerk 00")
                    Q[i] = '1'
                    cache = Q[i]
                if J[i - 2] == '0' and K[i - 2] == '1':
                    # KILL
                    #print("kill 00")
                    Q[i] = '0'
                    cache = Q[i]
                if J[i - 2] == '0' and K[i - 2] == '0':
                    print("ALARM")
                #print("NOW CACHE IS " + cache)
        else:
            #save zone
            Q[i] = cache
    #print(Q)    
    # reverse
    for i in range(len(Q)):
        unQ[i] = reverse_sig(Q[i])
    
    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

# ! WORKS
def sixth():
    C = getC()
    D = getD()
    Q = [ '9' for i in range(len(D))]
    unQ = [ '9' for i in range(len(D))]
    Q[0] = input("Input first of Q: ")
    if Q[0] == '0':
        unQ[0] = '1'
    else:
        unQ[0] = '0'
    cache = Q[0]
    for i in range(1, len(Q)):
        if C[i - 1] == '1' and C[i] == '0':
            Q[i] = D[i - 1]
            cache = Q[i]
        else:
            Q[i] = cache
    
    for i in range(len(Q)):
        if Q[i] == '1':
            unQ[i] = '0'
        elif Q[i] == '0':
            unQ[i] = '1'
        else:
            unQ[i] = Q[i]
    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

# ! WORKS
def seventh():
    C = getC()
    D = getD()
    Q = [ '9' for i in range(len(D))]
    unQ = [ '9' for i in range(len(D))]
    Q[0] = input("Input first of Q: ")
    if Q[0] == '0':
        unQ[0] = '1'
    else:
        unQ[0] = '0'
    cache = Q[0]
    for i in range(1, len(Q)):
        if C[i - 1] == '0' and C[i] == '1':
            Q[i] = D[i - 1]
            cache = Q[i]
        else:
            Q[i] = cache
    for i in range(len(Q)):
        if Q[i] == '1':
            unQ[i] = '0'
        elif Q[i] == '0':
            unQ[i] = '1'
        else:
            unQ[i] = Q[i]
    Q = "".join(Q)
    unQ = "".join(unQ)
    print("Q: " + Q)
    print("U: " + unQ)

if __name__ == '__main__':
    main()
