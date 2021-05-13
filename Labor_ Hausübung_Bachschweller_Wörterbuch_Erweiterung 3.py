woerterbuch_deutsch_zu_english = {"Winkel":"angle", "Sägeblatt":"blade", "Bautischler":"carpentry", "Möbeltischler":"cabinet maker", "Dübel":"dowel", "Holzfaser":"fibre"}
woerterbuch_englisch_zu_deutsch = {"angle":"Winkel", "blade":"Sägeblatt", "carpentry":"Bautischler", "cabinet maker":"Möbeltischler", "dowel":"Dübel", "fibre":"Holzfaser"}

Begriff = input("Welches Wort möchten Sie übersetzen?")

try:
    print(woerterbuch_deutsch_zu_english[Begriff])

except:
    try:
       print(woerterbuch_englisch_zu_deutsch[Begriff])
    
    except:
        print("nicht gefunden")







