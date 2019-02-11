import sys

hasil = []

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
    actual_score = 0
    i=1
    temp= int (s[i-1])
    while (i+1<=len(s)) :
        if (s[i]=='+' or s[i]=='-'):
            plusmin = True
        if ((s[i]=='*' or s[i]=='/') and plusmin):
            kurung = True
        score += give_score(s[i])
        actual_score += give_score(s[i])
        temp= eval(str(temp),s[i+1],s[i])
        i+=2    
    score -= abs(obj-temp)*3
    actual_score -= abs(obj-temp)
    if kurung :
        score-=1
        actual_score -= 1
    return score, actual_score

def cards_to_strnumber(arg): 
    if arg == 'A':
        return '1'
    elif arg == 'J':
        return '10'
    elif arg == 'Q':
        return '11'
    else:
        return '12'

