# Pi näherungsweise durch Leibniz-Reihe berechnen!

def leibniz(n):
    summe = 0
    
    for k in range(n):
        schritte = (-1) ** k / (2*k+1) # Formel Leibniz-Reihe!! k sind die Schritte, welche der Benutzer angeben muss.
        summe += schritte 
    return summe * 4 # mal 4 rechnen, ansonsten wären es pi/4

schritte = int(input("Anzahl der Schritte: ")) # je größerer die Zahl, umso genauer wird die Ausgabe

pi = leibniz(schritte)

print("Pi = ", pi)