import sys
from display import *

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
    score -= abs(obj-temp)*3
    if kurung :
        score-=1
    return score

def cards_to_number(argument): 
    switcher = { 
        A : "1",
        J : "10",
        Q : "11",
        K : "12",
    }
    return switcher.get(argument, "nothing") 

if __name__ == "__main__":
    hasil = []
    if len(sys.argv)==1:
        deck_maker()
        randomize_card()
        Solver24App().run()
        unsorted_list = []
        for i in range (4):
            temp = list_of_card[i][0]
            if (temp == 'A') or (temp == 'J') or (temp == 'Q') or (temp == 'K'):
                cards_to_number(temp)
            unsorted_list.append(temp)
        sorted_list = sorting(unsorted_list)
    elif len(sys.argv)==3 :
        file_input = sys.argv[1]
        file_output = sys.argv[2]

        f = open(file_input, "r")
        contents = f.read()
        f.close()
        sorted_list = sorting(contents.split())
    else :
        print("Wrong input format")

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
    
    if (op_list[0] == '+' or op_list[0] == '-') and (op_list[1] == '*' or op_list[1] == '/'):
        s= '('+sorted_list[0]+op_list[0]+sorted_list[1]+')'+op_list[1]+sorted_list[2]+op_list[2]+sorted_list[3]
    elif (op_list[1] == '+' or op_list[1] == '-') and (op_list[2] == '*' or op_list[2] == '/'):
        s = '('+sorted_list[0]+op_list[0]+sorted_list[1]+op_list[1]+sorted_list[2]+')'+op_list[2]+sorted_list[3]
    else:
        s = sorted_list[0]+op_list[0]+sorted_list[1]+op_list[1]+sorted_list[2]+op_list[2]+sorted_list[3]
    
    if len(sys.argv)==1:
        print(s)
    elif len(sys.argv)==3 :
        f = open(file_output, "w+")
        f.write(s)
        f.close()
    print(score)