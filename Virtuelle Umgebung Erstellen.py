
##################################################
# Virtuelle Umgebung Erstellen
##################################################

##################################################
# Aufgabe 1: Erstellen Sie eine virtuelle Umgebung mit Ihrem Namen und installieren Sie Python 3.
##################################################

 # conda create -n ma python=3
 # conda env list

##################################################
# Aufgabe 2: Aktivieren Sie die erstellte Umgebung.
##################################################

 # conda activate ma

##################################################
# Aufgabe 3: Listen Sie die installierten Pakete auf.
##################################################

 # conda list

##################################################
# Aufgabe 4: Installieren Sie gleichzeitig die aktuelle Version von Numpy und die Version 1.2.1 von Pandas.
##################################################

 # conda install numpy pandas=1.2.1

##################################################
# Aufgabe 5: Welche Version von Numpy wurde installiert?
##################################################

# conda list

##################################################
# Aufgabe 6: Aktualisieren Sie Pandas. Welche neue Version wird installiert?
##################################################

 # conda upgrade pandas
 # conda list


##################################################
# Aufgabe 7: Entfernen Sie Numpy aus der Umgebung.
##################################################

 # conda remove numpy

##################################################
# Aufgabe 8: Installieren Sie Seaborn und Matplotlib gleichzeitig in den neuesten Versionen.
##################################################

 # conda install seaborn matplotlib

##################################################
# Aufgabe 9: Exportieren Sie die Pakete Ihrer virtuellen Umgebung mit Versionsinformationen in eine yaml-Datei und prüfen Sie diese.
##################################################

 # conda env export > enviroment.yaml

##################################################
# Aufgabe 10: Löschen Sie die erstellte virtuelle Umgebung.
##################################################

 # conda deactivate
 # conda env remove -n ma
