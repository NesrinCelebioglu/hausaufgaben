
##################################################
# Pandas-Übungen
##################################################
import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Aufgabe 1: Laden Sie den Titanic-Datensatz aus der Seaborn-Bibliothek.
#########################################

df =sns.load_dataset("titanic")
df.head()
df.shape

#########################################
# Aufgabe 2: Ermitteln Sie die Anzahl der weiblichen und männlichen Passagiere im oben definierten Titanic-Datensatz.
#########################################

gesclecht_counts =df["sex"].value_counts()

#########################################
# Aufgabe 3: Ermitteln Sie die Anzahl der eindeutigen Werte für jede Spalte.
#########################################

einzigartige_werte =df.nunique()

#########################################
# Aufgabe 4: Finden Sie die eindeutigen Werte der Variablen 'pclass'.
#########################################
 
df["pclass"].nunique()
df["pclass"].unique()

#########################################
# Aufgabe 5: Ermitteln Sie die Anzahl der eindeutigen Werte der Variablen 'pclass' und 'parch'.
#########################################

df[["pclass","parch"]].nunique()

#########################################
# Aufgabe 6: Überprüfen Sie den Datentyp der Variablen 'embarked'. Ändern Sie den Typ zu 'category' und überprüfen Sie anschließend erneut den Datentyp.
#########################################

df["embarked"].dtype
str(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtype)
df.info()

#########################################
# Aufgabe 7: Zeigen Sie alle Informationen der Einträge, bei denen der Wert von 'embarked' 'C' ist.
#########################################

c_passagiere = df[df['embarked'] == 'C']
print(c_passagiere)


#########################################
# Aufgabe 8: Zeigen Sie alle Informationen der Einträge, bei denen der Wert von 'embarked' nicht 'S' ist.
#########################################

a = df[df["embarked"] != "S"]
a["embarked"].unique()

#########################################
# Aufgabe 9: Zeigen Sie alle Informationen der Passagiere, die jünger als 30 Jahre alt und weiblich sind.
#########################################

junge_frauen = df.loc[(df["sex"] == "female") & (df["age"] < 30)]

#########################################
# Aufgabe 10: Zeigen Sie alle Informationen der Passagiere, deren 'fare' größer als 500 oder deren 'age' größer als 70 ist.
#########################################

teure_oder_alte_passagiere = df.loc[(df["fare"] > 500) & (df["age"] >70)].head()

#########################################
# Aufgabe 11: Ermitteln Sie die Gesamtanzahl der fehlenden Werte für jede Spalte.
#########################################

fehlende_werte = df.isnull().sum()
print(fehlende_werte)

#########################################
# Aufgabe 12: Entfernen Sie die Variable 'who' aus dem DataFrame.
#########################################


df.drop("who", axis=1, inplace=True)

df = df.drop("who", axis=1)

#########################################
# Aufgabe 13: Füllen Sie die fehlenden Werte der Variablen 'deck' mit dem am häufigsten vorkommenden Wert (Mode) der Variablen 'deck'.
#########################################

df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"]


#########################################
# Aufgabe 14: Füllen Sie die fehlenden Werte der Variablen 'age' mit dem Median der Variablen 'age'.
#########################################

df["age"].fillna(df["age"].median(),inplace=True)
df["age"]

#########################################
# Aufgabe 15: Berechnen Sie die Summe, Anzahl und den Mittelwert der Variable 'survived' nach den Variablen 'pclass' und 'sex'.
#########################################

df.groupby(["pclass", "sex"]).agg({"survived":["sum", "count", "mean"]})

#########################################
# Aufgabe 16: Schreiben Sie eine Funktion, die 1 für Passagiere unter 30 Jahren und 0 für Passagiere ab 30 Jahren zurückgibt.
# Verwenden Sie diese Funktion mit apply und lambda, um eine neue Variable 'age_flag' im Titanic-Datensatz zu erstellen.
#########################################



def age_30(age):
    if age<30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x : age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

#oder

df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)


#########################################
# Aufgabe 17: Definieren Sie den Tips-Datensatz aus der Seaborn-Bibliothek.
#########################################


df1 =sns.load_dataset("tips")
df1.columns

#########################################
# Aufgabe 18: Berechnen Sie die Summe, das Minimum, das Maximum und den Durchschnitt der Variable 'total_bill' nach den Kategorien der Variable 'time' (Dinner, Lunch).
#########################################


df1.groupby(["time"]).agg({"total_bill":["sum","min","max","mean"]})

#########################################
# Aufgabe 19: Berechnen Sie die Summe, das Minimum, das Maximum und den Durchschnitt der Variable 'total_bill' nach den Variablen 'day' und 'time'.
#########################################


df1.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]})

#########################################
# Aufgabe 20: Berechnen Sie die Summe, das Minimum, das Maximum und den Durchschnitt der Variablen 'total_bill' und 'tip' für weibliche Kunden zur Lunch-Zeit nach 'day'.
#########################################

df1.loc[(df1["time"] == "Lunch") & (df1["sex"]== "Female")].groupby(["day"]).agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"],
                                                                            "Lunch" : lambda x:  x.nunqiue()})


#########################################
# Aufgabe 21: Wie ist der Durchschnitt der Bestellungen, bei denen 'size' kleiner als 3 und 'total_bill' größer als 10 ist?
#########################################


df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10)]["total_bill"].mean()

#########################################
# Aufgabe 22: Erstellen Sie eine neue Variable 'total_bill_tip_sum', die die Summe von 'total_bill' und 'tip' für jeden Kunden angibt.
#########################################


df1["total_bill_tip_sum"] = df1["total_bill"] + df1["tip"]

df1

#########################################
# Aufgabe 23: Berechnen Sie den Durchschnitt von 'total_bill' getrennt für Frauen und Männer.
# Erstellen Sie eine neue Variable 'total_bill_flag', die 0 ist, wenn der Wert unter dem Durchschnitt liegt, und 1, wenn er größer oder gleich dem Durchschnitt ist.
# Achtung! Für Frauen gilt der Durchschnitt der Frauen, für Männer der Durchschnitt der Männer.
# Beginnen Sie, indem Sie eine Funktion schreiben, die das Geschlecht und 'total_bill' als Parameter nimmt (mit if-else Bedingungen).
#########################################


# Durchschnittswerte für Frauen und Männer berechnen
f_avg = df[df["sex"]=="Female"]["total_bill"].mean()  # Durchschnitt der Frauen
m_avg = df[df["sex"]=="Male"]["total_bill"].mean()    # Durchschnitt der Männer

# Funktion definieren
def func(sex, total_bill):
    if sex=="Female":
        if total_bill < f_avg:
            return 0
        else:
            return 1
    else:  # Male
        if total_bill < m_avg:
            return 0
        else:
            return 1

# Neue Spalte 'total_bill_flag' erstellen
df["total_bill_flag"] = df[["sex","total_bill"]].apply(lambda x: func(x["sex"], x["total_bill"]), axis=1)

# Kontrolle
print(df[["sex","total_bill","total_bill_flag"]].head(10))

#########################################
# Aufgabe 24: Beobachten Sie die Anzahl der Personen unterhalb und oberhalb des Durchschnitts nach Geschlecht, basierend auf der Variable 'total_bill_flag'.
#########################################

df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})

#########################################
# Aufgabe 25: Sortieren Sie die Variable 'total_bill_tip_sum' absteigend und speichern Sie die obersten 30 Personen in einem neuen DataFrame.
#########################################

neu_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30] 
neu_df.shape