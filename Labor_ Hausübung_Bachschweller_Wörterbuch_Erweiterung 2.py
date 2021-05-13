#Erweiterung Wörterbuch um Möglichlichkeit, Einträge zu ergänzen bzw. zu löschen.

woerterbuch_deutsch = ["Winkel", "Sägeblatt", "Bautischler", "Möbeltischler", "Dübel", "Holzfaser"]
print(len(woerterbuch_deutsch))
      
woerterbuch_english = ["angle", "blade", "carpentry", "cabinet maker", "dowel", "fibre"]
print(len(woerterbuch_english))

running = True
while running:
    Eingabe = input("Befehl? [E]infügen, [L]öschen, [A]bfragen, [B]eenden: ")

    if Eingabe.lower() == "e":
        deutscher_Begriff = input("Welches deutsche Wort möchten Sie einfügen")
        woerterbuch_deutsch.append(deutscher_Begriff)
        englischer_Begriff = input("Welches englisches Wort möchten Sie einfügen")
        woerterbuch_english.append(englischer_Begriff)

    elif Eingabe.lower() == "l":
        Begriff = input("Welches Wort möchten Sie löschen?")

        Indexbegriff = 0

        Gesamtanzahl = len(woerterbuch_deutsch)

        while Indexbegriff < Gesamtanzahl:
            if woerterbuch_deutsch[Indexbegriff].lower() == Begriff.lower():
                break
            Indexbegriff +=1
            
        if Indexbegriff == Gesamtanzahl:
            
            Indexbegriff = 0
            
            while Indexbegriff < Gesamtanzahl:
                if woerterbuch_english[Indexbegriff].lower() == Begriff.lower():
                    break
                Indexbegriff +=1

        if Indexbegriff == Gesamtanzahl:
            print("nicht gefunden")
        
        woerterbuch_deutsch.remove(woerterbuch_deutsch[Indexbegriff])
        woerterbuch_english.remove(woerterbuch_english[Indexbegriff])
    
    elif Eingabe.lower() == "b":
        break
        

    else: 
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
            
    print(woerterbuch_deutsch,woerterbuch_english)

