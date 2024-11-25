# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 06:35:31 2024

@author: surya
"""

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    #print("bet",bet)
    #print("lucky_draw",lucky_draw)
    
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
        
print( " amount your account",account)
plt.plot(x,y)
plt.show()
