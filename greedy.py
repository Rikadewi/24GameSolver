def sorting(arr) :
    if len(arr)==0 :
        return []
    last = arr[len(arr)-1]
    arr = arr[:(len(arr)-1)]
    left = []
    right = []

    for i in range (0,len(arr)):
        if arr[i]>=last :
            left.append(arr[i])
        else :
            right.append(arr[i]) 
    
    left = sorting(left)
    hasil.append(last)
    right = sorting(right)
    return hasil

def eval(x1,x2,op):
    x1 = float(x1)
    x2 = float(x2)
    if op=='+' :
        return x1+x2
    elif op=='-' :
        return x1-x2
    elif op=='*' :
        return x1*x2
    elif op=='/' :
        if x2==0 :
            return -9999
        return x1/x2    

def give_score(op):
    if op=='+':
        return 5
    elif op=='-':
        return 4
    elif op=='*':
        return 3
    elif op=='/':
        return 2

def calc_score(s,obj):
    plusmin = False
    kurung = False
    score = 0
    i=1
    temp= int (s[i-1])
    while (i+1<=len(s)) :
        if (s[i]=='+' or s[i]=='-'):
            plusmin = True
        if ((s[i]=='*' or s[i]=='/') and plusmin):
            kurung = True
        score += give_score(s[i])
        temp= eval(str(temp),s[i+1],s[i])
        i+=2    
    score -= abs(obj-temp)
    if kurung :
        score-=1
    return score

if __name__ == "__main__":
    #sorted_list = sorting(list(map(str, input("24 Game Solver\nMasukan input: ").split())))
    #print(sorted_list)
    hasil=[]    
    hasill=0
    for a in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
        for b in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
            for c in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                for d in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
                    # hasil=[]
                    
                    sorted = sorting([str(a), str(b), str(c), str(d)])
                    sorted_list = sorted[len(sorted)-4:]
                    
                    #print(sorted_list)
                    # print('hasil', hasil)
                    
                    op_list = ['X','X','X']
                    score = -9999
                    for op in '+-*/':
                        #print(sorted_list[0]+op+sorted_list[1])
                        temp = calc_score([sorted_list[0],op,sorted_list[1]], 24-float(sorted_list[2])-float(sorted_list[3]))
                       # print('op1: ', temp)
                        if(temp > score):
                            score = temp
                            op_list[0] = op

                    score = -9999            
                    for op in '+-*/':
                        temp = calc_score([sorted_list[0],op_list[0],sorted_list[1],op,sorted_list[2]], 24-float(sorted_list[3]))
                        #print('op2: ', temp)
                        if(temp > score):
                            score = temp
                            op_list[1] = op

                    score = -9999            
                    for op in '+-*/':
                        temp = calc_score([sorted_list[0],op_list[0],sorted_list[1],op_list[1],sorted_list[2],op,sorted_list[3]], 24)
                        #print('op3: ', temp)
                        if(temp > score):
                            score = temp
                            op_list[2] = op
                    
                    '''
                    if (op_list[0] == '+' or op_list[0] == '-') and (op_list[1] == '*' or op_list[1] == '/'):
                        print('('+sorted_list[0]+op_list[0]+sorted_list[1]+')'+op_list[1]+sorted_list[2]+op_list[2]+sorted_list[3])
                    elif (op_list[1] == '+' or op_list[1] == '-') and (op_list[2] == '*' or op_list[2] == '/'):
                        print('('+sorted_list[0]+op_list[0]+sorted_list[1]+op_list[1]+sorted_list[2]+')'+op_list[2]+sorted_list[3])
                    else:
                        print(sorted_list[0]+op_list[0]+sorted_list[1]+op_list[1]+sorted_list[2]+op_list[2]+sorted_list[3])
                    print(score)
                    '''
                    #'''
                    #print(score)
                    hasill +=score
    print(hasill/(13*13*13*13))
    #'''                                                                                           