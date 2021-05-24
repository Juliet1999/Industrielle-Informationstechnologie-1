#Erweiterung des Wörterbuch-Programmes
#
# 1) Funktion zur Eingabe des Befehls
# 2) Funktion zur Eingabe des Suchbegriffs bzw. Wortes
# 3) Funktion zur Suche
# 4) Funktion zur Ausgabe

woerterbuch_deutsch_zu_english = ["Winkel", "Sägeblatt", "Bautischler", "Möbeltischler", "Dübel", "Holzfaser"]
      
woerterbuch_english_zu_deutsch = ["angle", "blade", "carpentry", "cabinet maker", "dowel", "fibre"]

def eingabe_befehl():
    running = False
    while running == False:
        Eingabe = input("Befehl? [E]infügen, [L]öschen, [A]bfragen, [B]eenden: ")
        Eingabe = Eingabe.lower()
        if Eingabe == "e":
            deutscher_Begriff = input("Welches deutsche Wort möchten Sie einfügen")
            woerterbuch_deutsch_zu_english.append(deutscher_Begriff)
            englischer_Begriff = input("Welches englisches Wort möchten Sie einfügen")
            woerterbuch_english_zu_deutsch.append(englischer_Begriff)
            
        elif Eingabe == "l":
            Suchbegriff = eingabe_suchbegriff()
            Indexbegriff = suche_begriff(Suchbegriff)
            try:
                woerterbuch_deutsch_zu_english.remove(woerterbuch_deutsch_zu_english[Indexbegriff])
                woerterbuch_english_zu_deutsch.remove(woerterbuch_english_zu_deutsch[Indexbegriff])
            except:
                print("Dieses Wort existiert nicht")
            
        elif Eingabe == "a":
            Suchbegriff = eingabe_suchbegriff()
            Indexbegriff = suche_begriff(Suchbegriff)
            try:
                ausgabe_begriff(Indexbegriff)
            except:
                print("Dieses Wort existiert nicht")
        else:
            running = True
            
def eingabe_suchbegriff():
    Begriff = input("Welches Wort möchten Sie eingeben?")
    return Begriff.lower()

def suche_begriff(Suchbegriff):
    
    Indexbegriff = 0

    Gesamtanzahl = len(woerterbuch_deutsch_zu_english)

    while Indexbegriff < Gesamtanzahl:
        if woerterbuch_deutsch_zu_english[Indexbegriff].lower() == Suchbegriff:
            break
        Indexbegriff +=1
                
    if Indexbegriff == Gesamtanzahl:
                
        Indexbegriff = 0
                
        while Indexbegriff < Gesamtanzahl:
            if woerterbuch_english_zu_deutsch[Indexbegriff].lower() == Suchbegriff:
                break
            Indexbegriff +=1    
    return Indexbegriff

def ausgabe_begriff(Uebersetzung):
    print(woerterbuch_english_zu_deutsch[Uebersetzung],"(EN)")
    print(woerterbuch_deutsch_zu_english[Uebersetzung],"(DE)")

eingabe_befehl()

        
        
        
        
        
        
        