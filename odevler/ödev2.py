### görev 1 ###

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

### görev 2 ###

text = "The goal is to turn data into information,and information into insight."
a = str(text.upper()).replace(".", " ").replace(",", " ").split()
print(a)

### görev 3 ###
Ist = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C","E"]
len(Ist)
a = Ist[0]
print(a)
b = Ist[10]
print(b)
c = Ist[0:4]
print(c)
Ist.pop(8)
print(Ist)
Ist.append(4)
print(Ist)
Ist.insert(8, "N")
print(Ist)

### görev 4 ###

dict = {"Christian": ["America", 18], "Daisy": ["England", 12], "Antonio": ["Spain", 22], "Dante" :["Italy", 25]}
dict.keys()
dict.values()
dict["Daisy"] = ["England", 13]
print(dict)
dict["Ahmet"] = ["Turkey", 24]
print(dict)
del dict ["Antonio"]
print(dict)

### görev 5 ###

l =[2, 13, 18, 93, 22]
def func(list):
     even_list = []
     odd_list = []
     for i in list:
          if i % 2 == 0:
               even_list.append(i)
          else:
                odd_list.append(i)
     return even_list, odd_list
even_list, odd_list = func(l)
print(func(l))


### görev 6 ###

students = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

 for index, student in enumerate(students, 1):
      if index <= 3 :
           print("Mühendislik_Fakültesi", ".", index, "ögrenci:", student ),
      else :
           print("Tip_Fakültesi", ".", index-3, "ögrenci:", student )

### görev 7 ###

ders_kodu = ["CMP1005", "PSY001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan =[30, 75, 150, 25]

list(zip(ders_kodu, kredi, kontenjan))

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
     print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjani {kontenjan} kisidir.")

### görev 8 ###

küme1 = set(["data", "python"])
küme2 = set(["data", "function", "qcut", "lambda", "pyhton", "miull"])

if küme1.issuperset(küme2):
     print(küme1.intersection(küme2))
else:
     print(küme2.difference(küme1))

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))