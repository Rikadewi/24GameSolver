from kivy.core.window import Window
import sys, os
import random
from kivy.clock import Clock, mainthread
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from test import *

Window.size = (1200,700)
Window.clearcolor = (0.1, 0.25, 0.1, 0.1)

script_dir = sys.path[0]

list_of_opr = ['+','-','*','/']
list_of_type = ['S','C','H','D']
list_of_number = ['A','2','3','4','5','6','7','8','9','J','Q','K']
list_of_card = []
history = []
card_deck = []
score_final = 0
score_actual = 0

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

def deck_maker():
    del(card_deck[:])
    for num in list_of_number:
        for ty in list_of_type:
            temp = num + ty
            card_deck.append(temp)

def draw_card(index):
	return os.path.join(script_dir, 'Cards/' + str(list_of_card[index]) + '.png')

def randomize_card():
    if not card_deck:
        pass
    else:
        del(history[:])
        del(list_of_card[:])
        for x in range (4):
            card = random.choice(card_deck)
            list_of_card.append(card)
    print(list_of_card)

def calculate():
    global score_final
    global score_actual
    sorted_list = []
    unsorted_list = []

    del(hasil[:])
    for i in range (4):
        temp = list_of_card[i][0]
        if (temp == 'A') or (temp == 'J') or (temp == 'Q') or (temp == 'K'):
            temp = cards_to_strnumber(temp)
        unsorted_list.append(temp)
    unsorted_list[0] = int(unsorted_list[0])
    unsorted_list[1] = int(unsorted_list[1])
    unsorted_list[2] = int(unsorted_list[2])
    unsorted_list[3] = int(unsorted_list[3])

    sorted_list = sorting(unsorted_list)

    print(sorted_list)

    op_list = ['X','X','X']
    score = -9999
    for op in '+-*/':
        #print(sorted_list[0]+op+sorted_list[1])
        temp, temp_final = calc_score([sorted_list[0],op,sorted_list[1]], 24-float(sorted_list[2])-float(sorted_list[3]))
        # print('op1: ', temp)
        if(temp > score):
            score = temp
            score_actual = temp_final
            op_list[0] = op

    score = -9999            
    for op in '+-*/':
        temp, temp_final = calc_score([sorted_list[0],op_list[0],sorted_list[1],op,sorted_list[2]], 24-float(sorted_list[3]))
        #print('op2: ', temp)
        if(temp > score):
            score = temp
            score_actual = temp_final
            op_list[1] = op

    score = -9999            
    for op in '+-*/':
        temp, temp_final = calc_score([sorted_list[0],op_list[0],sorted_list[1],op_list[1],sorted_list[2],op,sorted_list[3]], 24)
        #print('op3: ', temp)
        if(temp > score):
            score = temp
            score_actual = temp_final
            op_list[2] = op

    if (op_list[0] == '+' or op_list[0] == '-') and (op_list[1] == '*' or op_list[1] == '/'):
        s= '('+str(sorted_list[0])+op_list[0]+str(sorted_list[1])+')'+op_list[1]+str(sorted_list[2])+op_list[2]+str(sorted_list[3])
    elif (op_list[1] == '+' or op_list[1] == '-') and (op_list[2] == '*' or op_list[2] == '/'):
        s = '('+str(sorted_list[0])+op_list[0]+str(sorted_list[1])+op_list[1]+str(sorted_list[2])+')'+op_list[2]+str(sorted_list[3])
    else:
        s = str(sorted_list[0])+op_list[0]+str(sorted_list[1])+op_list[1]+str(sorted_list[2])+op_list[2]+str(sorted_list[3])

    score_final += score_actual
    is24 = False
    if eval(eval(eval(sorted_list[0],sorted_list[1],op_list[0]),sorted_list[2],op_list[1]),sorted_list[3],op_list[2]) == 24:
        is24 = True
        
    return s, is24

class MyCardDisplay(FloatLayout):
    def update_new(self):
        self.answerLbl.text = ''
        self.infoLbl.text = ''
    def update_calculate(self):
        answer, isdeletecard = calculate()
        self.totalLbl.text = 'Final score: ' + str(score_final)
        self.scoreLbl.text = 'Score:[b] ' + str(score_actual)
        self.answerLbl.text = 'Answer: ' + answer
        if (isdeletecard):
            for x in range (4):
                card = list_of_card[x]
                card_deck.remove(card)
                self.infoLbl.text = ''
        else:
            self.infoLbl.text = 'Answer is not 24, cards returned to deck'
        print("cards on deck:")
        print(card_deck)

class Solver24App(App):
    def build(self):
        return MyCardDisplay()
