# 1) Wörterbuch

# 1.1) Eingabe Suchbegriff (deutsch)
# 1.2) Bestimmung der Gesamtanzahl der Elemente (= maximaler Index)
# 1.3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 1.4) Wenn Element gefunden -> Index speichern
# 1.5) Zugriff auf Listenelement[Index] in Liste (englisches Wörterbuch)

woerterbuch_deutsch = ["Winkel", "Sägeblatt", "Bautischler", "Möbeltischler", "Dübel", "Holzfaser"]
print(len(woerterbuch_deutsch))
      
woerterbuch_english = ["angle", "blade", "carpentry", "cabinet maker", "dowel", "fibre"]
print(len(woerterbuch_english))

Begriff = input("Welches Wort möchten Sie übersetzen?")

Indexbegriff = 0

Gesamtanzahl = len(woerterbuch_deutsch)

while Indexbegriff < Gesamtanzahl:
    if woerterbuch_deutsch[Indexbegriff].lower() == Begriff.lower():
        Uebersetzung = Indexbegriff
        print(woerterbuch_english[Uebersetzung])
        break
    Indexbegriff +=1
    
if Indexbegriff == Gesamtanzahl:
    print("nicht gefunden")

