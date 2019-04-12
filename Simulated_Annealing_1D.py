# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:01:25 2018

@author: Max
"""

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

x=f(3); #beliebiger Startpunkt
xs=x;
t=0;
step=.01;
y=x;
T=100; #beliebige streng monotone Funktion
i=0;
mini=100000;

while i<1000:
    while T > 0: #Abbruchbedingung, muss pos Zahl sein, auch möglich: keine Veränderung xo; Wert erreicht, etc.
        y= y+step;
    
        if f(y)<=f(x):
            x=y
        if f(y)>f(x):
            if np.exp(-1*( (f(y)-f(x)) /T)): # das bewirkt, dass es unwahrscheinlich ist, das es sich verschlechter
                x=y;

        if f(x) < (f(xs)):
            xs=x;
        t=t+1;
        T = (20-.01*t); 
        

    i=i+1;
    T=20;
    if mini > f(x):
        mini= f(x);



x=np.linspace((mini-5),(mini+5) , 100000)
y=f(x)


plt.figure()
plt.plot(x,y)
plt.plot(mini, f(mini), "ob")
plt.show()


print (mini)