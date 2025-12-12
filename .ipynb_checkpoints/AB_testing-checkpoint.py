
###################################################
# PROJE: AB testing
###################################################
###################################################
#Veri Seti Açıklaması#

#Bir e-ticaret sitesinin reklam gösterimleri ve kullanıcı etkileşimlerini içeren bu veri seti, ziyaretçilerin gördükleri reklamlara tıklama sayıları ve elde edilen gelir bilgilerini içermektedir. Çalışmada iki farklı grup bulunmaktadır:
#Kontrol Grubu: Maksimum Teklif (Maximum Bidding) yöntemi uygulanmıştır.
#Test Grubu: Ortalama Teklif (Average Bidding) yöntemi uygulanmıştır.
#Veriler, ab_test_data.xlsx adlı Excel dosyasının ayrı sayfalarında bulunmaktadır.#
#Gösterim (Impression)		 Reklam görüntüleme sayısı
#Tıklama (Click)			 Görüntülenen reklama tıklama sayısı
#Satın Alma (Purchase)		 Reklama tıklama sonrası satın alma sayısı
#Gelir (Earning)			 Satın alma sonrası elde edilen gelir

###################################################

###################################################
# GÖREV 1: Veri Hazırlama ve İnceleme
###################################################
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)



df_control= pd.read_excel("C:/Users/nesri/OneDrive/Desktop/ders kaynaklari/6.hafta/ab_test_data.xlsx",sheet_name="Control Group")
df_test = pd.read_excel("C:/Users/nesri/OneDrive/Desktop/ders kaynaklari/6.hafta/ab_test_data.xlsx", sheet_name="Test Group")
df_control.head()
df_test.head()
df_control.shape
df_test.shape
df_control.info()
df_test.info()
df_control.describe().T
df_test.describe().T
df_control.isnull().sum()
df_test.isnull().sum()

df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control,df_test], axis=0,ignore_index=False)
df.head()
df.sort_values(by="group")
df.groupby("group").agg({"Purchase": "mean"})

###################################################
# GÖREV 2: A/B Testi İçin Hipotez Tanımlama
###################################################
df.groupby("group").agg({"Purchase": "mean"})


####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.

# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz
# Normallik Varsayımı :
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ
test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value=0.5891

test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9589, p-value = 0.1541

# Varyans Homojenliği :
# H0: Varyanslar homojendir.
# H1: Varyanslar homojen değildir.
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ
# Kontrol ve test grubu için varyans homojenliğinin sağlanıp sağlanmadığını Purchase değişkeni üzerinden test ediniz.


test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value=0.1083

# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

# Varsayımlar sağlandığı için bağımsız iki örneklem t testi (parametrik test) yapılmaktadır.
# H0: M1 = M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark yoktur.)
# H1: M1 != M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark vardır)
# p<0.05 HO RED
# p>0.05 HO REDDEDİLEMEZ

test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value = 0.3493

Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

# Varsayımlar sağlandığı için bağımsız iki örneklem t testi (parametrik test) yapılmaktadır.
# H0: M1 = M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark yoktur.)
# H1: M1 != M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark vardır)
# p<0.05 HO RED
# p>0.05 HO REDDEDİLEMEZ

test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value = 0.3493


####################################################
# GÖREV 4: Sonuclarin Degerlendirilmesi
#####################################################

# Adım 1: Hangi istatistiksel testi kullandığınızı ve bu testi seçme sebebinizi açıklayınız.
# t testi kullandik.

# Adım 2: Elde ettiğiniz test sonuçlarına dayanarak müşteriye hangi teklif stratejisini önerirsiniz?
# Test sonucuna göre maximum bidding mi yoksa average bidding mi daha etkili görünüyor? Tavsiyenizi gerekçelendirerek açıklayınız.

#HO reddedilemez. Kontrol grubu ve test grubu satın alma ortalamaları arasında istatiksel olarak anlamlı fark yoktur.
# Yaptığımız istatiksel testlerin sonucunda anlamlı bir fark olmadığını görebiliyoruz. Bu sonuçlara göre iki gruba yönelik çalışmalarını sürdürebilirler.


