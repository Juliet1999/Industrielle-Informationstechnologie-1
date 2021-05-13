# 1) Wörterbuch

# 1.1) Eingabe Suchbegriff (deutsch) oder Eingabe Suchbegriff (englisch)
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
        print(woerterbuch_english[Uebersetzung],"(EN)")
        break
    Indexbegriff +=1
    
if Indexbegriff == Gesamtanzahl:
    
    Indexbegriff = 0
    
    while Indexbegriff < Gesamtanzahl:
        if woerterbuch_english[Indexbegriff].lower() == Begriff.lower():
            Uebersetzung = Indexbegriff
            print(woerterbuch_deutsch[Uebersetzung],"(DE)")
            break
        Indexbegriff +=1

if Indexbegriff == Gesamtanzahl:
    print("nicht gefunden")