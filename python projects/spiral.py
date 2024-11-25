# -*- coding: utf-8 -*-um
"""
Created on Fri Oct 11 10:01:50 2024

@author: surya
"""
import turtle
turtle.bgcolor("black")
tur = turtle.Turtle()
import random

width=5
height=7

dot_distance=25

tur.penup()
list_color=["white","yellow","orange","grey","red","purple","green","pink","violet","blue"]

tur.setpos(-250,250)






def spiralprint(m,n):
    k=0
    l=0
    f=0
    tur.color("white")
    " k = index of starting row"
    " l = index of startinf colum"
    col=random.randint(0,8)
    tur.color(list_color[col])
    while(k<m and l<n):
        
        if(f==1):
            tur.right(90)
        #print first row from the remaing row
        for i in range(l,n):
            tur.dot()
            tur.forward(dot_distance)
            #print(a[k][i], end=" ")
        
        k+=1
        f=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(list_color[col])
        
        #printing the last from remaing colum
        for i in range(k,m):
            tur.dot()
            tur.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(list_color[col])
        if(k<m):
            #printing the last row from remaing rows
            for i in range(n-1,l-1,-1):
                tur.dot()
                tur.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m-=1
        tur.right(90)
        col=random.randint(0,8)
        tur.color(list_color[col])
        
        if(l<n):
            #printing the first colum the remaing colum
            for i in range(m-1,k-1,-1):
                tur.dot()
                tur.forward(dot_distance)
               # print(a[i][l],end=" ")
            l+=1
            
spiralprint(20,20)
turtle.done()
        
          
"""a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
    
    
spiral(4,4,a)"""
                
                
            
        
        
