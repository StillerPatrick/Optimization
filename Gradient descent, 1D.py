# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:21:01 2018

@author: Max
"""

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

x=f(3); #beliebiger Startpunkt
step=.01;
epsilon=.000005;
y=x;
i=0;

while i<1000:
    
    k= ((f(x+epsilon)-f(x))/(epsilon));
    if k<0:
        step= step - (.001*k);
    if k>0:
        step= step + (.001*k);
    
    y= y+step;
    if f(y)<=f(x):
        x=y
    i=i+1;
    
xr=x;
yr=f(x);
        
x=np.linspace((x-5),(x+5) , 100000)
y=f(x)


plt.figure()
plt.plot(x,y)
plt.plot(xr, yr, "ob")
plt.show()


print (yr)