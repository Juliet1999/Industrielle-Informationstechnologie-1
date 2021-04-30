# Aufgabe 1:
# Schreiben Sie ein Python-Program, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimt
# 3) eine zweite Zahl entgegen nimt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient kleinere Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)

Name = input("Bitte geben Sie Ihren Namen ein:")
print("Hello", Name)

Zahl1_string = input("Eingabe der ersten Zahl:")
Zahl1 = int(Zahl1_string) # int = nur ganze Zahlen
Zahl2_string = input("Eingabe der zweiten Zahl:")
Zahl2 = float(Zahl2_string) # float = Zahlen auch mit Komma

# Berechnung der Summe
Summe = Zahl1 + Zahl2

# Berechnung der Differenz
if Zahl2 >= Zahl1:
    Differenz = Zahl2 - Zahl1
elif Zahl2 <= Zahl1:
    Differenz = Zahl1 - Zahl2

# Berechnung des Produktes
Produkt = Zahl1 * Zahl2

# Berechnung des Quotienten
if Zahl2 >= Zahl1:
    Quotient = Zahl1 / Zahl2
elif Zahl2 <= Zahl1:
    Quotient = Zahl2 / Zahl1
    
# Ausgabe der Ergebnisse
print("Summe", Summe)
print("Differenz", Differenz)
print("Produkt", Produkt)
print("Quotient", Quotient)

