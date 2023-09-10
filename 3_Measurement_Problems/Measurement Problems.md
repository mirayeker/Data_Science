# Measurement Problems

---

**Social Proof:** Sosyal ispat kavramı

**The Wisdow of Corwds** : Toplunun bilgeliğine olan inanç(Pazarlıkta kendini kabul ettirmiş bir inançtır.)

# Rating Products

## Bir Ürünü Satın Aldıran Nedir ?

---

- Ürün puanlarının hesaplanması
- Ürünlerin sıralanması
- Ürün detay sayfalarındaki kullanıcıların yorumlarının sıralanması
- Sayfa süreç ve etkileşim alanlarının tasarımları
- Özellik denemeleri
- Olası aksiyonların ve reaksiyonların test edilmesi

Rating Products:(Ürün puanlama): Olası faktörleri göz önünde bulundurarak ağırlıklı ürün puanlama

### TIME-BASED WEIGHTED AVERAGE

> **Puan zamanlarına göre ağırlıklı ortalama**, farklı dönemlerde elde edilen puanların önemine göre ağırlıklandırıldığı bir ortalama türüdür. Bu yöntemde, her puan dönemine ait ağırlık verilir ve puanlar bu ağırlıklarla çarpılır. Sonrasında bu ağırlıklı puanlar toplanır ve toplam ağırlıkla bölünerek ağırlıklı ortalama elde edilir.
> 

### USER - BASED WEIGHTED AVERAGE

> **Kullanıcı ağırlıklı ortalama**, farklı kullanıcılardan veya gruplardan alınan verilerin her bir kullanıcının/grubun önemine göre ağırlıklandırıldığı bir ortalama türüdür. Bu yöntemde, her kullanıcıya/gruba ait veri setine bir ağırlık verilir ve veriler bu ağırlıklarla çarpılır. Sonrasında bu ağırlıklı veriler toplanır ve toplam ağırlıkla bölünerek kullanıcı ağırlıklı ortalama elde edilir.
> 

---

# Sorting Products

Sorting Products:(Ürün sıralama): Olası faktörleri göz önünde bulundurarak ağırlıklı ürün sıralama

> bayesian average rating: puan dağılınlarının üzerinden ağırlıklı bir şekilde olasılıksal ortalama hesabı yapar.
> 

# Sorting Reviews

İnsanların satın alma davranışının en ciddi etkileyen faktörlerden birisidir. 

Peki neye göre sıralıyoruz? 

> User Quality Score adını verdiğimiz, yani benim için 1 film izleyen kullanıcıyla 100 film izleyen kullanıcı aynı değildir gibi senaryolarda kullanıcılara verecek olduğumuz skrlar olabilir.
> 

<aside>
💡 Ya  da ilgili iş birimiyşe alakalı oluşturulabilecek farklı skorlar olabilir. Dolayısıyşa buradaki sıralamayı etkileyen şey sadece tek bir faktör değildir.

</aside>

<aside>
💡 Biz Buanların yüksek ya da düşük olmasıyla ilgilnemiyoruz, pazar yeri olarak kullanıcılara en doğru sosyal ispatı ulaştırmaya çalışyoruz. Dolayısıyla düşük ve yüksek olmasıyla ilgilenmiyoruz.

</aside>

### Üst-Alt Farkı Skoru (Up-Down Difference Score):

# Review 1: 600 up 400 down total 1000

# Review 2: 5500 up 4500 down total 10000

<aside>
💡 Up-Down Diff Score = (up ratings) − (down ratings)

</aside>

! Uygulaması bait ama yanlılık barındırır. 
Yukarıdaki Reviewler karşılaştırıldığında 2. review daha yüksek sırada olur (5550-4500 = 1000 score vardır ama [1.review](http://1.review) yüzdelik (%60 vs %55) olarak bize daha anlamlı bilgi verir.)

### Ortalama Puanı (Avarege Rating):

<aside>
💡 Score = Average rating = (up ratings) / (all ratings)

</aside>

# Review 1: 2 up 0 down total 2 → oran(1)

# Review 2: 100 up 1 down total 101 → oran (0,9)

Sayı yüksekliğini veya frekans yüksekliğini göz önünde bulunduramadı.

### Wilson Alt Sınır Puanı (Wilson Lower Bound Score)

Wilson Lower Bound Score hesapla- Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.

- Hesaplanacak skor ürün sıralaması için kullanılır.

<aside>
💡  Not:Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

</aside>

# AB Testi (AB Testing)

---

## Temel istatistik Kavramları

### Sampling (Örnekleme):

İstatistikte, bir popülasyonun tamamının incelenmesi yerine, popülasyonun belirli bir alt kümesini (örneklem) incelemeyi ifade eder.

### Betimsel İstatistikler (Descriptive Statistic):

Değişkenin dağılımı ile ilgili bilgi edinebiliriz. 

<aside>
💡 describe(): fonksiyonu veri setindeki sayısal sutunları bularak temel istatistiksel bigileri verir.

</aside>

! Aykırı Değeri gözlemlemek çin median ve mean arasında karşılaştırma yapabiliriz. Eğer arada uçurum gibi bir varsa bu işlikte bir terslik ar diyebiliriz. 😊

### Confidence Intervals (Güven Aralıkları):

Anakütle parametresinin tahmini değerini (istatistik) kapsayabilecek iki sayıdan oluşan bir aralık bulunmasıdır. 

<aside>
💡 örneğin, bir popülasyonun ortalama veya varyansı tahmini değeri ile ilgili belirli bir güven düzeyi içindeki olası değerlerini ifade eden aralıklardır

</aside>

### Correlation (Korelasyon):

Değişkenler arasındaki ilişki, bu ilişkinin yönü ve şiddeti ile ilgili bilgiler sağlayan istatiksel bir yöntemdir. 

<aside>
💡 Koreleasyon değeri -1 ile 1 değerleri arasında yer alır. 0 korelasyon olmadığını belirtir.

</aside>

![Untitled](Measurement%20Problems%2024d8c7e28ed74108b2c56fc90362a7e8/Untitled.png)

> Pozitif Korelasyon: Değişkenin değerleri artarken diğer değişkenin de artacağı anlamına gelir.
> 

> Negatif Korelasyon: Değişkenin değerleri artarken diğer değişkenin azalacağı anlamına gelir.
> 

## Hipotez Testleri (Hypothesis Testing)

### Hipotez Nedir: Bir inanışı bir savı test etmek için kullanılan isttiatiksel yöntemlerdir.

<aside>
💡 Grup karşılaştırmalarında **temel amaç olası farklılıkların** şans eseri ortaya çıkıp çıkmadığını göstermeye çalışmaktadır.

</aside>

1. **Anlamlılık Düzeyi (Significance Level - α):** Anlamlılık düzeyi, bir hipotez testinin kabul edilebilir bir hata yapma olasılığını belirtir. Genellikle α sembolü ile temsil edilir. Örneğin, α = 0.05 olduğunda, bu %5 anlam düzeyine karşılık gelir ve bir test sonucunda hata yapma olasılığı %5'i geçmemelidir.
2. **p-Değeri (p-value):** p-değeri, bir hipotez testinin sonucunu ifade eden istatistiksel bir ölçüdür. p-değeri, gözlemlenen verilere dayalı olarak, null hipotezin doğruluğunun sınamasını sağlar. Eğer p-değeri, belirlenen anlamlılık düzeyinden (α) küçükse (p < α), null hipotez reddedilir. Yani, bu durumda, veriler null hipoteze karşı yeterli kanıtı sağlıyor demektir.

**Örnek olarak, α = 0.05 anlamlılık düzeyi belirlenmişse ve bir test sonucunda p-değeri 0.03 çıkarsa, bu durumda p-değeri α'dan küçük olduğu için null hipotez reddedilir. Yani, veriler null hipotezi desteklemiyor ve alternatif hipotez kabul edilir.**