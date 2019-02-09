from kivy.core.window import Window
import sys, os
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

Window.size = (1200,700)
Window.clearcolor = (0.1, 0.25, 0.1, 0.1)

script_dir = sys.path[0]

list_of_opr = ['+','-','*','/']
list_of_type = ['S','C','H','D']
list_of_number = ['A','2','3','4','5','6','7','8','9','J','Q','K']
list_of_card = []
history = []
card_deck = []

def deck_maker():
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
            card_deck.remove(card)
            history.append(card_deck)
            list_of_card.append(card)
        print(card_deck)

class MyCardDisplay(FloatLayout):
    pass

class Solver24App(App):
    def build(self):
        return MyCardDisplay()

def StartDisplay():
    Solver24App().run()
    
# if __name__ == "__main__":
#     _24SolverApp().run()