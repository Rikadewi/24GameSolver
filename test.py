import sys

hasil = []
#variabel untuk menampung hasil sorting

#untuk menghitung hasil dari suatu ekspresi, menerima dua buah integer dan sebuah operator
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

#memberikan score berdasarkan operator
def give_score(op):
    if op=='+':
        return 5
    elif op=='-':
        return 4
    elif op=='*':
        return 3
    elif op=='/':
        return 2

#menghitung score akhir dan score semu berdasarkan nilai operator dan selisih jawaban dengan 24
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

#megubah nilai dari kartu yang bukan merupakan angka
def cards_to_strnumber(arg): 
    if arg == 'A':
        return '1'
    elif arg == 'J':
        return '10'
    elif arg == 'Q':
        return '11'
    else:
        return '12'

