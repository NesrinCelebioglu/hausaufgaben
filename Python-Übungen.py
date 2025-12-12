###############################################
# Python-Übungen
###############################################


###############################################
# Aufgabe 1: Untersuchen Sie die Arten von Datenstrukturen
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Pyhton", "Mascine Learning", "Data Science"}
type(s)

###############################################
# Aufgabe 2: Wandeln Sie den gegebenen String vollständig in Großbuchstaben um. Ersetzen Sie Kommas und Punkte durch Leerzeichen und trennen Sie den Satz anschließend in einzelne Wörter.
###############################################

text = "The goal is to turn data into information,and information into insight."
a = str(text.upper()).replace(".", " ").replace(",", " ").split()
print(a)
###############################################
# Aufgabe 3: Führen Sie für die gegebene Liste die folgenden Aufgaben aus.
###############################################

Ist = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C","E"]

# Schritt 1: Überprüfen Sie die Anzahl der Elemente in der gegebenen Liste.
len(Ist)

# Schritt 2: Rufen Sie die Elemente am Index 0 und am Index 10 auf.
a = Ist[0]
print(a)
b = Ist[10]
print(b)

# Schritt 3: Erstellen Sie aus der gegebenen Liste die Liste ["D", "A", "T", "A"].
c = Ist[0:4]
print(c)

# Schritt 4: Löschen Sie das Element am Index 8.
Ist.pop(8)
print(Ist)

# Schritt 5: Fügen Sie ein neues Element hinzu.
Ist.append(4)
print(Ist)

# Schritt 6: Fügen Sie an Index 8 erneut das Element „N“ ein.
Ist.insert(8, "N")
print(Ist)

###############################################
# Aufgabe 4: Wenden Sie die folgenden Schritte auf die gegebene Wörterbuchstruktur an.
###############################################

dict = {"Christian": ["America", 18], "Daisy": ["England", 12], "Antonio": ["Spain", 22], "Dante" :["Italy", 25]}

# Schritt 1: Greifen Sie auf die Schlüsselwerte zu.
dict.keys()

# Schritt 2: Greifen Sie auf die Werte zu.
dict.values()

# Schritt 3: Aktualisieren Sie den Wert 12 des Schlüssels „Daisy“ auf 13.
dict["Daisy"] = ["England", 13]
print(dict)

# Schritt 4: Fügen Sie einen neuen Eintrag mit dem Schlüssel „Ahmet“ und dem Wert [Turkey, 24] hinzu.
dict["Ahmet"] = ["Turkey", 24]
print(dict)

# Schritt 5: Löschen Sie „Antonio“ aus dem Wörterbuch.
del dict ["Antonio"]
print(dict)

###############################################
# Aufgabe 5: Schreiben Sie eine Funktion, die eine Liste als Argument erhält,die ungeraden und geraden Zahlen der Liste in separate Listen einsortiert und diese Listen zurückgibt.
###############################################
l = [2, 13, 18, 93, 22]

def trenne_gerade_und_ungerade(liste):
    gerade_liste = []
    ungerade_liste = []
    for zahl in liste:
        if zahl % 2 == 0:
            gerade_liste.append(zahl)
        else:
            ungerade_liste.append(zahl)
    return gerade_liste, ungerade_liste

gerade_liste, ungerade_liste = trenne_gerade_und_ungerade(l)
print(trenne_gerade_und_ungerade(l))


###############################################
# Aufgabe 6: In der unten stehenden Liste befinden sich die Namen der erfolgreichsten Studierenden der Fakultät für Ingenieurwesen und der Fakultät für Medizin.
#Die ersten drei Studierenden repräsentieren die Rangfolge in der Ingenieurfakultät,#die letzten drei Studierenden gehören zur Rangfolge der Medizinfakultät.
#Geben Sie die Platzierungen der Studierenden fakultätsspezifisch unter Verwendung von enumerate aus.
###############################################
students = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli"]

for index, student in enumerate(students, 1):
    if index <= 3:
        print("Fakultät für Ingenieurwesen.", index, "Student:", student)
    else:
        print("Fakultät für Medizin.", index - 3, "Student:", student)


###############################################
# Aufgabe 7: Unten sind 3 Listen gegeben.
#In den Listen stehen jeweils der Kurscode, die Kreditpunkte und die Kontingentinformationen eines Kurses.
#Geben Sie die Kursinformationen mithilfe von zip aus.
###############################################

kurs_code = ["CMP1005", "PSY001", "HUK1005", "SEN2204"]
kredit = [3, 4, 2, 4]
kontingent = [30, 75, 150, 25]

list(zip(kurs_code, kredit, kontingent))

for kurs, kredite, kont in zip(kurs_code, kredit, kontingent):
    print(f"Der Kurs {kurs} hat {kredite} Kreditpunkte und ein Kontingent von {kont} Studierenden.")


###############################################
# Aufgabe 8: Unten sind 2 Mengen gegeben.
# Sie sollen eine Funktion definieren, die
#- die gemeinsamen Elemente ausgibt, wenn die 1. Menge die 2. Menge enthält,
#- andernfalls die Differenz der 2. Menge zur 1. Menge ausgibt.
###############################################

menge1 = set(["data", "python"])
menge2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def menge_vergleich(set1, set2):
    if set1.issuperset(set2):
        print("Gemeinsame Elemente:", set1.intersection(set2))
    else:
        print("Elemente, die nur in Menge 2 sind:", set2.difference(set1))

menge_vergleich(menge1, menge2)