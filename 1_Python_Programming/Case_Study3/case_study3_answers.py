#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı (level based) yeni satış tanımları
# oluşturmak ve bu yeni satış tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.
# Örneğin: Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek isteniyor.
#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = pd.read_excel("1_Python_Programming/Case_Study3/miuul_gezinomi.xlsx")
df.head()
df.info
# Soru 2:Kaç unique şehirvardır? Frekanslarınedir?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()


# Soru 3:Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df.groupby("ConceptName").agg({"SaleId": "count"})

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış
df.groupby("SaleCityName").agg({"Price": "sum"}).astype(int)

# Soru6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"}).astype(int)

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru 8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımındaPRICE ortalamalarınedir?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})


#############################################
# GÖREV 2: satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
#############################################
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins,labels=labels)

#############################################
# GÖREV 3: Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız
#############################################

# Şehir-Concept-EB Score kırılımında ücret ortalamaları
df.groupby(["SaleCityName","ConceptName", "EB_Score"]).agg({"Price" : ["mean", "count"]})

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
df.groupby(["SaleCityName","ConceptName", "Seasons"]).agg({"Price" : ["mean", "count"]})

# Şehir-Concept-CInday kırılımında ücret ortalamaları
df.groupby(["SaleCityName","ConceptName", "CInDay"]).agg({"Price" : ["mean", "count"]})

#############################################
# GÖREV 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

df_agg = df.groupby(["SaleCityName","ConceptName", "Seasons"]).agg({"Price":"mean"}).sort_values("Price", ascending=False)

#############################################
# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()

df_agg.reset_index(inplace= True)
df_agg.head(20)

#############################################
# GÖREV 6: Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.

df_agg["sales_level_based"]= df_agg[["SaleCityName","ConceptName", "Seasons"]].agg(lambda x: "_".join(x).upper(),axis=1)

#############################################
# GÖREV 7: Personaları segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz
df_agg["SEGMENT"]= pd.qcut(df["Price"], 4, labels= ["D", "C", "B", "A"])
df_agg.groupby("SEGMENT").agg({"Price" : ["mean", "max", "sum"]})

#############################################
# GÖREV 8: Oluşan son df'i price değişkenine göre sıralayınız.
# "ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?
#############################################

## Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
df_agg[df_agg["sales_level_based"] == new_user]

#Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır
new_user2 = "GIRNE_YARIM PANSIYON_LOW"
#df_agg.loc[df_agg['SaleCityName'].str.contains("Girne")]

df_agg[df_agg["sales_level_based"] == new_user2]




