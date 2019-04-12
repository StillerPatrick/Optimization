import numpy as np
import matplotlib.pyplot as plt
import json
%matplotlib inline


#hier muss rein nach was genau optimiert werden soll
#bis jetzt wird das von hand eingegeben
#das ist leider sehr limitiert für die ergebnisse
print("hier eingeben nach was optimiert werden soll ")
print("1=A0; 2=Pulse length , 3=beides")

path = "/bigdata/picongpuService/hr5806/laserWakefield/scan_0003/sim_0001/params.json"
newpath =path.split("/")
def findenvonscan(list):
    for i in range(len(list)):
        if "scan" in list[i]:
            return  i

scanschnipsel = newpath[findenvonscan(newpath)]
schnipseldesschnipsels = scanschnipsel.split("_")
schnipsel = int(schnipseldesschnipsels[1])+1
if schnipsel <1000:
    rückführungsschnipsel = str(0)+ str (schnipsel)
if schnipsel <100:
    rückführungsschnipsel = str(0) +str(0) +str(schnipsel)
if schnipsel < 10:
    rückführungsschnipsel = str(0) + str(0)+str(0) +str(schnipsel)
schnipseldesschnipsels = schnipseldesschnipsels[0] + ("_") + rückführungsschnipsel
newpath[findenvonscan(newpath)] = schnipseldesschnipsels
newpath = '/'.join(newpath)

print(newpath)



print(".json datei wird gesucht")
with open('/bigdata/picongpuService/hr5806/laserWakefield/scan_0003/sim_0001/params.json', encoding='utf-8') as data_file:
    supersecretdata = json.loads(data_file.read())
print("die top secret daten wurden gefunden")
supersecretint = 5 #gedacht als einheit nach wie vielen der werten optimiert werden soll. oder wie wollt ihr es mir mitteilen?
#meines wissens nach kann man ja nur an 5 werten rumspielen....

while True:
    try :
        supersecret_A0 = (supersecretdata["_A0"]["values"])
        print ("_A0",supersecret_A0)
        break;
    except KeyError:
        supersecretint=supersecretint-1
        break;
while True:
    try:
        supersecretWAVE_LENGTH_SI =(supersecretdata["WAVE_LENGTH_SI"]["values"])
        print ("WAVE_LENGHT_SI",supersecretWAVE_LENGTH_SI)
        break;
    except KeyError:
        supersecretint=supersecretint-1
        break;
while True:
    try:
        supersecretPULSE_LENGTH_SI = (supersecretdata["PULSE_LENGTH_SI"]["values"])
        print ("PULSE_LENGHT_SI", supersecretPULSE_LENGTH_SI)
        break;
    except KeyError:
        supersecretint=supersecretint-1
        break;
while True:
    try:
        supersecretBASE_DENSITY_SI = (supersecretdata["BASE_DENSITY_SI"]["values"])
        print("BASE_DENSITY_SI", supersecretBASE_DENSITY_SI)
        break;
    except KeyError:
        supersecretint=supersecretint-1
        break;
while True:
    try:
        supersecretTBG_STEPS = (supersecretdata["TBG_STEPS"]["values"])
        print("TBG_STEPS", supersecretTBG_STEPS)
        break;
    except KeyError:
        supersecretint=supersecretint-1
        break;

if supersecretint ==0:
    print("Du hast keine Daten eingegeben....... Ich kann damit nichts anfangen :(")
print("du hast", supersecretint, "daten zu verarbeitung eingegeben")


print("schau ob text lädt")
data = np.loadtxt("/bigdata/picongpuService/kossag14/laserWakefield/scan_0004/sim_0001/run/simOutput/e_energyHistogram_all.dat")
#data =np.loadtxt("/bigdata/picongpuService/hr5806/laserWakefield/scan_0003/sim_0001/run/simOutput/e_energyHistogram_all.dat")
print("ja macht er")

time = data[:, 0]
energy = np.linspace(0, 100, 1024)
count = data[:, 2:-2]

i=0
timee=0;
for elements in time:
    timee=timee+1
    
    
def malen(data, energy, count,i,n):
    plt.figure(n)
    plt.plot(energy,np.abs( count[i, :]))
    plt.yscale('log')
    plt.xlabel('E[keV]')
    plt.ylabel('#e')
    plt.show

def breite(count, i, minima):
    maxi=.5*minima
    a=0;
    while count[i,a]!=minima:
        a=a+1
        
    b=a
    while count[i,a]>maxi:
        a=a-1
    while count[i,a]>maxi:
        b=b+1
    return (b-a)
def lokalesminimum(count, i):
    groeste=count[i,50]
    for t in range (49):
        if groeste<count[i,(50+t)]:
            groeste=count[i,(50+t)]
    return groeste
n=0
while i<timee:
    print("Bild:", n)
    print("zeitschritt", i*100)
    malen(data, energy, count,i,n);
    #malen ist dafür da alles zu malen
    minima =(np.max(count[i,:]))
    print("globales maxima",minima)
    print("vom globalen breite",breite(count,i,minima)*97.6562) #diese 97,irgendwas sind im moment noch hardgecoded, weil ich es nicht schaffe es aus dem programm zu lesen, glaube der beginnn wird als kommentar gewertet
    if i*100==10000:
        print ("lokales maximum, hinten", lokalesminimum(count,i))
        print("breite vom lokalen",breite(count, i, lokalesminimum(count,i))*97.6562 )
    i=i+10;
    n=n+1
    
