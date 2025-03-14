
###################################################
# PROJE: Rating Product & Sorting Reviews in Amazon
###################################################
###################################################
# İş Problemi
###################################################

#İş Problemi
# E-ticaret platformlarında, ürünlere verilen puanların doğru bir şekilde hesaplanması ve
# yorumların etkili bir şekilde sıralanması büyük önem taşır. Bu, müşteri memnuniyetini artırır,
# satıcıların ürünlerinin öne çıkmasını sağlar ve kullanıcıların daha sorunsuz bir alışveriş
# deneyimi yaşamasına yardımcı olur. Ancak, yanıltıcı veya yanlış sıralanmış yorumlar,
# ürün satışlarını olumsuz etkileyebilir ve hem maddi kayıplara hem de müşteri kaybına neden olabilir.
# Bu projede, ürün puanlarını güncel yorumlara göre ağırlıklandırarak hesaplamayı ve yorumları etkili bir şekilde sıralamayı amaçlıyoruz.


###################################################
# Veri Seti Hikayesi
###################################################

# Bu projede, bir e-ticaret platformundan alınan ürün değerlendirme verilerini kullanacağız.
# Veri seti, elektronik kategorisindeki bir ürüne ait kullanıcı puanlarını ve yorumlarını içermektedir.

"""Veri seti aşağıdaki değişkenleri içerir:
reviewerID: Kullanıcı ID’si
asin: Ürün ID’si
reviewerName: Kullanıcı Adı
helpful: Faydalı değerlendirme derecesi
reviewText: Değerlendirme
overall: Ürün rating’i
summary: Değerlendirme özeti
unixReviewTime: Değerlendirme zamanı
reviewTime: Değerlendirme zamanı
day_diff: Değerlendirmeden itibaren geçen gün sayısı
helpful_yes: Değerlendirmenin faydalı bulunma sayısı
total_vote: Değerlendirmeye verilen oy sayısı
"""

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


df = pd.read_csv("C:/Users/nesri/downloads/amazon_review.csv")
df.head()
df.tail()
df.shape
df.info()
df.describe().T
df.columns

# rating dagılımı#
df["overall"].value_counts()

###################################################
# GÖREV 1: Güncel Yorumlara Göre Ortalama Puanı Hesaplayın.
###################################################

# Bu görevde, ürünün ortalama puanını güncel yorumlara göre ağırlıklandırarak
# hesaplayacak ve mevcut ortalama puanla karşılaştıracaksınız.

###################################################
# Adım 1: Ürünün mevcut ortalama puanını hesaplayın.
###################################################

df["overall"].mean()
# 4.587589013224822 #

###################################################
# Adım 2: Tarihe göre ağırlıklı ortalama puanı hesaplayın. Daha yeni yorumlara daha fazla ağırlık verin.
###################################################

df.info()

# yorum sonrası ne kadar gün geçmiş

df["reviewTime"].min()
df["reviewTime"].max()
df["reviewTime"] = pd.to_datetime(df["reviewTime"])
current_Date =df["reviewTime"].max()
df["days"] = (current_Date - df["reviewTime"]).dt.days
df["days"].describe().T

df["day_diff"].describe().T


q1= df["days"].quantile(0.25)
q2= df["days"].quantile(0.50)
q3= df["days"].quantile(0.75)
df["days"].describe().T

# zaman bazlı ortalama ağırlıkların belirlenmesi
def weighted_average_time_based(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["days"] <= 280, "overall"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["days"] > 280) & (dataframe["days"] <= 430), "overall"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["days"] > 430) & (dataframe["days"] <= 600), "overall"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["days"] > 600), "overall"].mean() * w4 / 100


weighted_average_time_based(df)
#4.595593165128118#
weighted_average_time_based(df, 30, 28, 22, 20)
#4.6018735292998905#
weighted_average_time_based(df, 32, 28, 22, 18)
#4.606864305471843#

###################################################
# Adım 3: Ağırlıklandırılmış ortalama puan ile mevcut ortalama puanı karşılaştırın ve yorumlayın.
###################################################
df["overall"].mean()
#4.587589013224822#


"""Zaman bazlı ağırlıklı ortalama (4.6069), mevcut ortalama puandan (4.5876) biraz daha yüksek. 
yeni yorumların genellikle daha yüksek puanlar içerdiğini ve 
son dönemde ürünün daha olumlu bir şekilde değerlendirildiğini göstermektedir.
"""


###################################################
# Görev 2: Ürün için Ürün Detay Sayfasında Görüntülenecek 20 Review'i Belirleyiniz.
###################################################
###################################################
# Adım 1 : helpful_no Değişkenini Üretiniz
###################################################

"""
total_vote, bir yoruma verilen toplam oy sayısıdır.
helpful_yes, yorumun faydalı bulunma sayısıdır.
helpful_no değişkeni, toplam oy sayısından faydalı oy sayısını çıkararak hesaplanır.
"""

df["helpful_no"] =df["total_vote"] - df["helpful_yes"]
df.head()
###################################################
# Adım 2: score_pos_neg_diff, score_average_rating ve wilson_lower_bound skorlarını hesaplayın ve veri setine ekleyin.
###################################################

"""
 score_pos_neg_diff: Faydalı oy sayısı ile faydalı bulunmayan oy sayısı arasındaki fark.
 average_rating_score: Faydalı oy sayısının toplam oy sayısına oranı.
 wilson_lower_bound: Wilson Alt Sınırı, yorumun güvenilirliğini ölçen bir istatistiksel yöntemdir.
 """

# score_pos_neg_diff

def score_pos_neg_diff(up, down):
    return up - down
df["score_pos_neg_diff"] = df.apply(lambda x: score_pos_neg_diff(x["helpful_yes"], x["helpful_no"]), axis=1)



# score_average_rating

def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)




# wilson_lower_bound

def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)
df["wilson_lower_bound"] = df.apply(lambda x:wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

df["wilson_lower_bound"].describe().T

##################################################
# Adım 3: Wilson Alt Sınırı'na göre en yüksek skora sahip ilk 20 yorumu belirleyin ve sonuçları yorumlayın.
###################################################

df.sort_values("wilson_lower_bound", ascending=False).head(20)
"""
İlk sıradaki yorum, Wilson Alt Sınırı değeri 0.95754 değeri ile en yüksek güvenilirliğe sahiptir.
Bu yorumun toplam 2020 oy alıp 1952'sinin "helpful_yes" olması, yani büyük oranda faydalı görülmesi dikkat çekmektedir.
Bu durum, bu yorumun oldukça güvenilir ve faydalı bulunduğunu gösteriyor.
Ortalama puanı 5.0, yani en yüksek seviyede bir değerlendirme almıştır.

WLB ile yapılan sıralamalarda ilk siralarda en çok oy alan yorumlar yer alıyor. 
Aynı zamanda faydalı bulunma oranı da dikkate alınmıştır. 
Aynı zamanda score_average_ratinge göre sıralama yapsaydık gözlem 5 gözlem 4 ün önüne geçecekti 
fakat burda 4. gözlemde daha çok oylama yapıldığı için WBL hesabında 5'in önüne geçmiştir.

Listenin alt sıralarında Wilson Alt Sınırı değeri 0.56 - 0.65 aralığına düşüyor.
Bu yorumların ortak özelliği, daha az sayıda oy almış olmaları.
5 puan alan bazı yorumların Wilson Alt Sınırı düşük çünkü çok az oy almışlar (örneğin 5 oy alıp tamamı "helpful" olan yorumlar var).
Bu durum, daha fazla oy almanın güvenilirlik açısından önemli olduğunu gösteriyor.
Düşük oy sayısı, yorumların istatistiksel olarak güvenilirliğini zayıflatıyor.

Wilson Lower Bound sıralaması, güvenilir ve faydalı yorumları öne çıkarmada etkili bir yöntemdir.
Yüksek oy alan ve faydalı bulunan yorumlar üst sıralarda yer alıyor.
Düşük oy sayısına sahip yorumlar, faydalı olsa bile güven aralığı düşük olduğu için sıralamada geriye düşüyor.
Eğer bir platformda en güvenilir yorumları göstermek istiyorsak, WLB değerine göre sıralama mantıklı bir yöntemdir.
"""









