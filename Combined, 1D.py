# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 12:53:39 2018

@author: Max
"""

import random
from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

x=f(3); #beliebiger Startpunkt
xs=x;
t=0;
step=.01;
y=x;
epsilon=.000005;
T=100; #beliebige streng monotone Funktion, evtl. ändern, siehe unten
i=0;
mini=100000;

while i<1000:
    while T > 0: #Abbruchbedingung, muss pos Zahl sein
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
        l= random.randint(0,1);
        if l==0:
            step= step;
        
        if l==1:
            step= (-step);
        k= ((f(x+epsilon)-f(x))/(epsilon)); #idee: anhnd der steigung die schrittweite ändern
        # geht in die richtung gradentenverfahren
        if k<0:
            step= step - (.001*k);
        if k>0:
            step= step + (.001*k);
        

    i=i+1;
    T=20;
    if mini > f(x):
        mini= f(x);
    if i >100:
        step = -.01;
    if i > 200:
        step = .5;
    if i> 300:
        step = -.5;
    if i> 400:
        step=100;
    if i> 500:
        step=-100;
    if i>600:
        x=-x;
    if i>700:
        step =1000;
    if i>800:
        step=-1000;
    if i>900:
        step=0;
    if i>1000:
        t= random.randint(1,10000);
        step=t*500;
    if i>5000:
        step=.00001;



x=np.linspace((mini-5),(mini+5) , 100000)
y=f(x)


plt.figure()
plt.plot(x,y)
plt.plot(mini, f(mini), "ob")
plt.show()


print (mini)
