

# Virtuelle Umgebung Erstellen

# Aufgabe 1: Erstellen Sie eine virtuelle Umgebung mit Ihrem Namen und installieren Sie Python 3.

 # conda create -n ma python=3
 # conda env list


# Aufgabe 2: Aktivieren Sie die erstellte Umgebung.


 # conda activate ma


# Görev 3: Yüklü paketleri listeleyiniz.


 # conda list


# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.


 # conda install numpy pandas=1.2.1



# Görev 5: İndirilen Numpy'ın versiyonu nedir?


# conda list


# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?

 # conda upgrade pandas
 # conda list



# Görev 7: Numpy'ı environment'tan siliniz.

 # conda remove numpy



# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel versiyonları ile indiriniz.


 # conda install seaborn matplotlib


# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.

 # conda env export > enviroment.yaml


# Görev 10: Oluşturduğunuz environment'i siliniz.


 # conda deactivate
 # conda env remove -n ma
