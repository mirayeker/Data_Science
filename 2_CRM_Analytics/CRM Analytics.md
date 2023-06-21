# CRM Analytics

---

## CRM: Müşteri İlişkileri yöntemi (Customer Relationship Management)

CRM Çerçevesinde Karşımıza Gelebilecek Çalışmalar

- Müşteri yaşam döngüsü optimizasyonları (customer lifecyle/journey/funnel)
- İletişim (dil,renk,görseller, kampanyalar)
- Müşteri edinme/bulma çalışmaları
- Müşteri elde tutma (terk) çalışmaları
- Çapraz Satış (cross-sell), üst satış (up-sell)
- Müşteri segmentasyon çalışmaları

<aside>
📌 Müşteriler ile ilişkiyi veriye dayalı yönetmektir. Aslında bir bakıma strateji geliştirmeyi sağlar, bu da daha fazla müşteri, daha fazla kazançsağlar. Yani özetle daha az çabayla daha fazla kaynak yaratmak olacaktır.

</aside>

## KPLs - Key Performance Indicators (Temel Performans Göstergeleri)

Şirket, departman ya da çalışanların performanlarını değerlendirmek için kullanılan matematiksel göstergeleridir. 

KPI Örnekleri: 

- Customer Acquisition Rate (Müşteri Kazanma Oranı)
- Customer Retention Rate (Müşteri Elde Tutma Oranı)
- Customer Churn Rate (Müşterei Terk Oranı)
- Conversion Rate (Dönüşüm Oranı)
- Growth Rate (Büyüme Oranı)

## Kohort Analizi (Analysis of Cohort)

Cohort: Ortak özelliklere sahip bir grup insan.

Cohort Analizi:  Ortak insanlara sahip bir grup insan davranışının analizidir.

## RFM ile Müşteri Segmentasyonu ( Customer Segmentation with RFM)

### RFM Nedir?

- RFM: Recency, Frequency, Monetary
- RFM Analizi Müşteri segmentasyonu için kullanılan bir tekniktir.
- Müşterilerin satın alma alışkanlıkları üzerinden gruplara ayrılması ve bu gruplar özelinde stratejiler geliştirebilmesini sağlar.
- CRM çalışmları için birçok başlıkta veriye dayalı aksiyon alma imkanı sağlar.

<aside>
📌 Basit, kural tabanlı müşteri segmantasyon tekniğidir.

</aside>

### RFM Teknikleri:

- Recency : Yenilik
- Frequency : Sıklık (İşlem Sayısı)
- Monetary: Parasal Değer

### RFM Skorları

3 Metriği (Recency,Frequency,Monetary) hepsini aynı cinsten ifade etmeye çalışacağız yani standartlaştıracağız (RFM skoru elde edeceğiz)

<aside>
📌 **`qcut`** fonksiyonu genellikle veri analizi ve segmentasyon süreçlerinde kullanılır. Verilerinizi belirli sayıda eşit büyüklükteki gruplara bölmek istediğinizde, **`qcut`** fonksiyonunu kullanabilirsiniz. Küçükten büyüğe sıralar. **`qcut`** fonksiyonunun en önemli parametreleri **`x`** (bölünmek istenen veri), **`q`** (kaç grup olacağı), ve **`labels`** (gruplara atanacak etiketler) şeklindedir. Fonksiyon, verileri belirtilen grup sayısı (q) temelinde böler ve her grup için belirtilen etiketi atar.

</aside>

> RFM ile skorlar üzerinden segmentler oluşturmak:
> 
> 
> ![Untitled](CRM%20Analytics%201038bbd947fc4fd88c5adaa2b44377f4/Untitled.png)
> 

<aside>
📌 İki boyutlu R ve F değerlerine bakarak oluşturuyoruz. zaten bizimle etkileşim halinde olan bir müşteriye daha fazla satış gerçekleştirebiliriz. Ama bunların olmadığı müşterinin monetary değerine bakmak pek anlamlı olmayacaktır..

</aside>

## Müşteri Yaşam Boyu Değeri  (Customer Lifetime Value)

- Bir müşterinin bir şirketle kurduğu ilişki-iletişim süresince bu şirkete kazandıracağı parasal değerdir.

> Nasıl Hesaplanır? :  Satın alma başına ortalama kazanç * satın alma sayısı
> 

<aside>
📌 Koyu renk ile yazılanlar sabit değerlerdir.

</aside>

- CLTV =  (Customer Value/ **Churn Rate**) x Profit Margin

! Profit Margin → Şirketin müşterilerle yaptığı alışverişlerde varsaydığı bir kar marjıdır.

- Customer Value = Avarage Order Value x Purchase Frequency
- Avarege Order Value = Total Price / Total Transaction
- Purchase Frequency = Total Transaction / **Total Number of Customers**
- **Churn Rate** = 1- Repeat Rate
- Repeat Rate= Birden fazla alışveriş yapan müşteri sayısı /  Tüm müşteriler
- Profit Margin = Total Price * **0.10** (sabit değer, örneğin şirket satışlardan %10 kar ettiğini ifade etmiş.

![Untitled](CRM%20Analytics%201038bbd947fc4fd88c5adaa2b44377f4/Untitled%201.png)

<aside>
📌 Sonuç olarak her bir müşteri için hesaplanacak olan CLTV değerlerine göre bir sıralama yapıldığında ve CLT değerlerine göre belirli noktalardan bölme işlemi yapılarak gruplar oluşturulduğunda müşterimiz segmentlere ayrılmış olacaktır.

</aside>

## Müşteri Yaşam Boyu Değeri Tahmini (Customer Lifetime Value Prediction)

### Zaman Projeksiyonlu Olasılıksal Lifetime Value Tahmini

customer value = satın alma sayısı  * satın alma başına ortalama kazanç

(Customer Value = Purchase Frequency * Avarage Order Value)

CLTV = (Customer Value / Churn Rate) x Profit Margin 

CLTV = Expected Number Of Transaction * Expected Average Profit 

CLTV = BG/NBD Model * Gamma Gamma Submodel 

### BG/NBD ile Beklenen İşlem Sayısı (Beta Geometric/Negative Binominal Distritubition with Expected Number of Transaction)

<aside>
📌 BG/NBD Modeli, expected Number of Transaction için iki süreci olasılıksal olarak modeller. 

Transaction Process(Buy) + Dropout Process (Till you die)

</aside>

### Transaction Process(Buy):

- Alive oldugu sürece, belirli bir zaman periyodunda, bir müsteri tarafından
gerçekleştirilecek ișlem sayısı transaction rate parametresi ile possion dağılır.
- Bir müsteri alive oldugu sürece kendi transaction rate'i etrafinda rastgele satın alma
yapmaya devam edecektir.
- Transaction rate'ler her bir müsteriye göre deisir ve tüm kitle için gamma dailir (r,a)

### Dropout Process (Till you die):

- Her bir müsterinin p olasılığı ile dropout rate (dropout probability)' vardır.
- Bir müşteri alıșveriş yaptıktan sonra belirli bir olasılıkla drop olur.
- Dropout rate'ler her bir müşteriye göre değişir ve tüm kitle için beta dağılır (a,b)

### Gamma Gamma Submodel:

Bir müşterinin ișlem bașına ortalama ne kadar kar getirebileceğini tahmin etmek için kullanılır.

CLTV = Expected Number of Transaction * Expected Average Profit
CLTV = BG/NBD Model * Gamma Gamma Submodel

- Bir müşterinin işlemlerinin parasal değeri (monetary) transaction value’larının ortalamasi etrafında rastgele dağılır.
- Ortalama transaction value, zaman içinde kullanıcılar arasinda değişebilir fakat tek bir kullanıcı için değişmez.
- Ortalama transaction value tüm müşteriler arasında gamma dagılır.