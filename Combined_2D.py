# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:11:48 2018

@author: Max
"""

import random
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #doch wird genutzt, das ist ein falscher fehler
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def f(x,y):#das ist die funktion
    return np.sin(x)*np.cos(y)+np.cos(x)

  
epsilon=.000005; #ganz kleine pos. Zahl
t=20; #Zähler der Anzahl der Durchläufe
T=(20-.01*t); #eine nach unten durchlaufene Beschreibung der Durchläufe, wird als Wahrscheinlichkeit mitgenutzt
i=0; #Zähler der Anzahl der Durchläufe der Durchläufe (Programm)
mini=1000000; #Zahl die bisher kleinsten Wert speichert
step = .00001; #schrittweite, wird später verändert
z = f(0,0); #beliebiger startpunkt, z ist anfänglich tiefster punkt
x=0;
y=0;
xstep=1;
ystep=1;
bug=0;
xr=0;
yr=0;
way=0; #zum überprüfen welche variabel optimiert werden soll, noch nicht fertig, noch nicht verwendet
       #im endgültigen Programm hoffentlich nicht so verwendet

while i<1000:
    if way ==0:
        while T > 0:
            #simulated Annealing
            x=x+step*xstep
            y=y+step*ystep
            z= f(x,y);
            if f(x,y) >=z:
                #f(x,y) =f((x+(step*xstep)), (y+(step*ystep)));
                x= x+step*xstep;
                y=y+step*ystep;
            if z> f(x,y):
                if np.exp(-1*( ((z-f(x,y))) /T)):
                    #f(x,y) =f(x+(step*xstep), y+(step*ystep));
                    x= x+step*xstep;
                    y=y+step*ystep;
            t=t+1;
            T = (20-.01*t); 
            l= random.randint(0,1);
            #zum ausgleichen von der geplannten richtung, wird im laufe des programmes ja sowies unwahrscheinlicher schlechter zu werden
            if l==0:
                step= step;
            if l==1:
                step= (-step);
            #berechnung der schrittweite
            if ((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f((x+epsilon), (y+epsilon)-f(x,y))))) <0:
                #print ("die wurzel ist schuld!");
                bug=bug+1;
                T=0;
                break;
            if ((epsilon)/math.sqrt((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f((x+epsilon), (y+epsilon)-f(x,y))))))>np.pi:
                #print("der arcsin ist schuld!");
                bug=bug+1;
                break;
            if (np.arcsin((epsilon)/math.sqrt((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f((x+epsilon), (y+epsilon)-f(x,y))))))) <(np.pi/2):
                #print("der tan ist schuld!");
                bug=bug+1;
                break;
            k= np.tan(np.arcsin((epsilon)/math.sqrt((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f((x+epsilon), (y+epsilon)-f(x,y)))))))
            if k<0:
                step= step - (((epsilon)/math.sqrt((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f((x+epsilon), (y+epsilon))-f(x,y)))))*k); #oben nachschauen was falsch
                stepx= (np.sin(np.arctan(((f(x+epsilon,y)-f(x,y)/epsilon)))));
                stepy=(np.sin(np.arctan(((f(x,y+epsilon)-f(x,y)/epsilon)))));
            if k>0:
                step= step + (((epsilon)/math.sqrt((2*epsilon*epsilon)+((f(x+epsilon, y+epsilon)-f(x,y))*(f(x+epsilon, y+epsilon)-f(x,y)))))*k);
                stepx=(np.sin(np.arctan(((f(x+epsilon,y)-f(x,y)/epsilon)))));
                stepy=(np.sin(np.arctan(((f(x,y+epsilon)-f(x,y)/epsilon)))));
            
        i=i+1;
        T=20;
        if mini > f(x,y):
            mini= f(x,y);
            xr=x;
            yr=y;
            
        #das sind nur versuche die schrittweite anzupassen
        if i >100:
            step = -.01;
        if i > 200:
            step = .5;
        if i>300:
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
            step=t*50000;
        if i>5000:
            step=.00001;
    
    if way ==1:
        print("warte auf das update...")
    if way ==2:
        print("warte auf das update")
    
       
# grafische Darstellung:
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange((xr-5),(xr+ 5), 0.25)
Y = np.arange((yr-5),(yr+5) , 0.25)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)


surf = ax.plot_surface(X, Y, Z , cmap=cm.coolwarm,linewidth=0, antialiased=False)

ax.set_zlim((mini-2), (mini+2))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))



plt.show()

if way ==0:
    print("Es wurden beide Variabeln optimiert")
if way ==1:
    print("Es wurde die x-variabel optimiert")
if way ==2:
    print("es wurde die y-variabel optimiert")
print("Der niedrigste z-Wert (Achse nach oben) liegt bei: ", mini)
print("Dies kommt beim x-Wert (Achse nach vorne) von: ", xr, " und beim y-Wert von: ",yr, "vor")
print("Fun Fact: von", i, "Durchläufen mussten mindestens", bug, "vorzeitig abgebrochen werden, weil python sonst Probleme mit der Berechnung bekommt")
        
        
