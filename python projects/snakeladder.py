# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import random
 
end=100
def show_board():
    img=Image.open("C:/Users/surya/Downloads/download.png")
    img.show()
    
def check_ladder(points):
    if points==1:
        print("ladder")
        return 38
    elif points==4:
        print("ladder")
        return 14
    elif points==8:
        print("ladder")
        return 30
    elif points==21:
        print("ladder")
        return 42
    elif points==28:
        print("ladder")
        return 76
    elif points==50:
        print("ladder")
        return 67
    elif points==71:
        print("ladder")
        return 92
    elif points==88:
        print("ladder")
        return 99
    else:
        #not a ladder
        return points
    
def check_snake(points):
    if points==32:
        print("snake")
        return 10
    elif points==36:
        print("snake")
        return 6
    elif points==48:
        print("snake")
        return 26
    elif points==62:
        print("snake")
        return 18
    elif points==88:
        print("snake")
        return 24
    elif points==95:
        print("snake")
        return 56
    elif points==97:
        print("snake")
        return 78
    else:
        #not a snake
        return points
        
def reached_end(points):
    if points==end:
        return True
    else:
        return False
            
            
            
        
    
    
def play():
    he=input("enter your name")
    she=input("enter your name")
    pp1=0
    pp2=0
    turn=0
    
    while(1):
        if turn%2==0:
            print(he,"your turn")
            choice=input("press 1 to continue,0 to quit")
            if choice==0:
                print(he,"scored",pp1)
                print(she,"scored",pp2)
                print("quiting the game")
                break
            dice = random.randint(1, 6)
            print(dice,"dice showed")
            pp1=pp1+dice
            
            pp1=check_ladder(pp1)
            
            pp1=check_snake(pp1)
            
            if pp1>end:
                pp1=end
                
            print(he,"your score",pp1)
            
            if(reached_end(pp1)):
                print(he,"won the game")
                break
        else:
            print(she,"your turn")
            choice=input("press 1 to continue,0 to quit")
            if choice==0:
                print(he,"scored",pp1)
                print(she,"scored",pp2)
                print("quiting the game")
                break
            dice = random.randint(1, 6)
            print(dice,"dice showed")
            pp2=pp2+dice
            
            pp2=check_ladder(pp2)
            
            pp2=check_snake(pp2)
            
            if pp2>end:
                pp2=end
                
            print(he,"your score",pp2)
            
            if(reached_end(pp2)):
                print(she,"won the game")
                break 
        turn=turn+1
            
            
            
                
    
show_board()
play()