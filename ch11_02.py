import turtle as t                          #2019775036
from winsound import B                      #양민철
 
freq = {"c4": 262, "d4":294, "e4":330, "f4":349, "g4": 392, "a4":440, "b4":494, "c5":523, "d5":587 }
 
def play_freq(n):
    Beep(freq[n],300)
 
def key_1():
    play_freq("c4")
def key_2():
    play_freq("d4")
def key_3():
    play_freq("e4")
def key_4():
    play_freq("f4")
def key_5():
    play_freq("g4")
def key_6():
    play_freq("a4")
def key_7():
    play_freq("b4")
def key_8():
    play_freq("c5")
def key_9():
    play_freq("d5")
 
t.setup(600,600)
s = t.Screen()
 
s.onkey(key_1,"1")
s.onkey(key_2,"2")
s.onkey(key_3,"3")
s.onkey(key_4,"4")
s.onkey(key_5,"5")
s.onkey(key_6,"6")
s.onkey(key_7,"7")
s.onkey(key_8,"8")
s.onkey(key_9,"9")
s.listen()
