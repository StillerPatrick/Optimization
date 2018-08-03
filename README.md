# Optimization
Ziel der Optimierung war einen Wert aus dem Energie-Histogramm zu optimieren. Dabei sollten möglichst wenig Iterationen verwendet werden, da eine Simulation sehr lange dauert. Dabei werden verschiedene Heuristiken verwendet, um möglichst das globable Maximum zu finden. Die verwendeten Heuristiken hängen dabei von der Anzahl der zu optimierenden Freiheitsgraden der Funktion ab.
Bei der Optimierung hier wird nur die Suche nach dem Maximum beschrieben, da es für die Suche durch negieren der Ausgangswerte auch für die Suche nach dem Minimum genutzt werden kann.
Es wurde generell gegen nicht-deterministische Optimierungsmethoden wie bspw. Monte Carlo entschieden, da diese eine Menge Iterationen benötigen und in diesem Fall gegen die oben genannten Bedingungen verstoßen.
# Problem mit einem Freiheitsgrad
Bei Problemen mit einem Freiheitsgrad wird eine Mischuns aus "Simulated Annealing"-Verfahren und Gradientenverfahren benutzt.
Beim Gradientenverfahren wird die Steigung an einer Stelle dazu genutzt um die Richtung der weiterführenden Optimierung zu bestimmen. Das Problem bei dieser Heuristik ist, dass sie unter Umständen nur ein lokales Optimum findet und nicht das gesuchte, globale Optimum.
Beim  „Simulated Annealing“-Verfahren wird versucht nicht in einem lokalen Minimum zu enden, weswegen es dort die Möglichkeit gibt, sich vorübergehend zu verschlechtern. Dies wird dadurch ermöglicht, dass man eine streng fallende Funktion T als Schrittzähler wählt. Je größer die Verschlechterung ist und je später man im Programmablauf ist, desto kleiner ist die Wahrscheinlichkeit sich zu verschlechtern.
Die Mischung besteht daraus, dass beim "Simulated Annealing"-Verfahren der nächst auszuwertende Punkt durch das Gradientenverfahren bestimmt wird. Damit man aber nicht in einem lokalen Maximum endet, kann es im Programm zufällig dazu kommen, dass der nächste zu prüfende Punkt in der entgegengesetzten Richtung liegt.
Ein weiterhin bestehende Problem ist die dynamische Anpassung der Schrittweite. Eine mögliche Idee ist die Orientierung an den möglichen Optimierungsgrenzen(noch sind keine vorhanden) und anhand der differnz der beiden Grenzen eine anfängliche Schrittweite zu berechnen.
# Problem mit zwei Freiheitsgraden
Bei diesem Problem reicht die das oben beschriebene Gradientenverfahren nicht mehr aus. Der Winkel zwischen der x1x2-Ebene (x3=0) und der Graden, die bei der Veränderung des ursprünglichen Punktes um Epsilon (ganz kleine pos. Zahl entsteht) ensteht berechnet. Die Formel dazu ist
Dies wird in x-,y- und xy-Richtung berechnet. Dadurch hat man einen 
# Probleme mit n Freiheitsgraden
# Quellen
