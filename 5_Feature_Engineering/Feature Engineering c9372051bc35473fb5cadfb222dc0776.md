# Feature Engineering

---

### Feature Engineering : Özellikler üzerinde gerçekleştirilen çalışmalar

### Data Pre-Processing: Çalışmalar öncesi verinin uyun hale getirilmesi sürecidir.

<aside>
💡 If Your Data Is Bad, Your Machine Learning Tools Are Useless 🙂

</aside>

<aside>
💡 Applied machine learning is basically feature engineering - Andrew Ng

</aside>

---

## Outliers (Aykırı Değerler)

Verideki genel eğilmin oldukça dışınaa çıkan değerlere denir.

! Özellikle doğrusal problemlerde aykırı değerlerin etkisi daha şiddetli olur. (Ağaç yöntemlerinde daha azdır.)

### Aykırı Değerler Neye göre belirlenir.

- Sektör Bilgisi
- Standart SApma Yaklaşımı
- Z-Skoru yaklaşımı
- Boxplot (interquartile range- IQR) yöntemi → Tek değişkenli olarak
- LOF → çok değişkenli olarak

### Aykırı Değer Problemlerini Çözme:

- Baskılama Yöntemi (re-assigment with threshold): Alt ve üst sınırların değerini aykırı değere atar. (Replace eder.)
- Çok Değişkenli Aykırı Değer Analizi (Local outlier Factor): Tek başına aykırı olmayacak değerler birlikte ele alındığında aykırı olabilir. (Mesela 17 yaşında birinin 3 defa evlenmesi)
    - LOF : Gözlemleri bulundukları konumun yoğunluk tabanlı skorlayarak aykırı değerlere ulaşmamızı sağlar.
    - A noktası açıkca görünüyor ki komşularına oldukça uzaktır. Bu sebeple aykırı değer diyebiliriz.
        
        ![Untitled](Feature%20Engineering%20c9372051bc35473fb5cadfb222dc0776/Untitled.png)
        
    - Peki LOF ile yakaladığımız değerleri nasıl handle edebiliriz?
        - Yakalanan değerlerin boyutu küçükse silebilirz ama büyükse ?
        - Baskılama yöntemi ile doldurabiliriz ama hangi değerle dolduracağız bir tane gözlem birimiyle doldursak duplicate problemi oluşacak ve veride gürültü oluşturacağız ?
        
        <aside>
        💡 Ağaç yöntemi ile çalışıyorsak aykırı değerlere hiç dokunmak tercih edilebilir. Eğer probleme göre bunlar göz ardı edilmemesi gerekiyorsa, IQR yöntemi ile tüm değişkenlere ufak bir dokunabiliriz.
        
        </aside>
        
        <aside>
        💡 Peki ya Doğrusal yöntemler kullanıyorsak? O zaman aykırı değerler ciddi bir problemdir, aykırı değerleri doldurmaktan ziyade  az ise silinebilir, doldurak yerine de baskılama yöntemi tercih edilebilir.
        
        </aside>
        
        > Gözlem sayısı çok olduğunda baskılama yöntemi kullanmak çok mantıklı olmayacaktır, gözlem sayısı az ise LOF ile bakıldıktan sonra o aykırı değerler çıkarılmalıdır.
        > 
        

 

---

## Missing Values (Eksik Değerler)

Gözlemlerde eksiklik olması durumunu ifade etmektedir.

Eksik Veri Problemi Nasıl Çözülür?

- Silme
- Değer Atama Yöntemleri (Basit Atama Yöntemleri, ortalama, median gibi değerler atanır.)
- Tahmine Dayalı Yöntemler (Makine öğrenmesi veya istatistiksel yöntemlere dayanır.)

Eksik veride dikkat edilmesi gereken nokta: EKSİK VERİNİN RASSALLIĞININ İNCELENMESİ

> Eksik verinin rassallığını incelemek, eksik değerlerin oluşma sebeplerini anlamak ve veri setindeki eksikliklerin sistematik bir düzeni olup olmadığını belirlemek amacıyla yapılır. (Örnneği bir kredi kartı analizi yapılacak, ve bir bireyin hiç kredi kartı yok bu durumda gözlem birimi null’dır, bu null değer doldurulmamalıdır!! )
> 

### Eksik Değer Problemini Çözme

Tıpkı aykırı değer probleminde olduğu gibi, eğer ağaca dayalı yöntemler kullanılıyorsa, bu durumda missing value’lar göz ardı edilebilir.

! Kategorik değişkenler için yapılabilecek en mantıklı yaklaşım modu ile doldurmaktır.

- Tahmine Dayalı Yöntemlerde Bir modelleme tekniği kullanılacağı için dikkat edilmesi gereken noktalar:
    1. Kategorik değişkenlerin one-hot ya da label  encoder uygulanması gerekir.
    2. KNN uygulayacağımız için verilerin standartlaştırılması gerekir. 

---

## Encoding

Değişkenlerin temsil şekillerinin değiştirilmesi

### Label Encoding:

Elimizdeki kategorik (nominal veya ordinal) değişkenleri sayısal değerler ile temsil etmektir. (Mesela cinsiyet: kadın, erkek → kadın:0, erkek:1)

> **Nominal Veriler:** Nominal veriler, sıralı bir yapısı olmayan verilerdir. Örneğin, ülkelerin isimleri (Türkiye, Fransa, İngiltere) nominal verilere örnektir. Label encoding bu durumda uygun değildir, çünkü bu verilerin sıralı bir yapısı yoktur. (Bu durumda one- hot encoding ile dönüştürülmesi daha uygundur.)
> 

```jsx
nunique() -> fonskiyonu nan değerleri bir sınıf olarak görmez.
unique() -> fonksiyonu ise nan değerleri de bir sınıf olarak görür. 
```

### One Hot Encoding

One-hot encoding, kategorik verileri sayısal forma dönüştürmek için kullanılan bir kodlama tekniğidir. Bu yöntem, her bir kategoriye ayrı bir sütun atayarak, o kategorinin varlığını 1, yokluğunu ise 0 ile temsil eder. (! Kullanılmasının asıl nedeni, sınıflar arasında bir fark yoksa mesela; Türkiye, Fransa, İtalya arasında bir üstünlük farkı yoktur biz bunları 1,2,3 diye verirsek model oluştururken hataya sebebiyet verebiliriz.)

- Nominal veriler (sıralı olmayan kategorik veriler) için uygundur.
- Dikkat edilmesi gereken bir konu vardır:  Dummy Değişken Tuzağı:
    - Dummy değişken tuzağı, one-hot encoding sırasında ortaya çıkabilen bir durumdur. Bu durum, kategorik değişkenlerin birbirine bağımlı hale gelmesi sonucu oluşur. Özellikle, eğer bir kategori, diğer kategorilerin toplamıyla ifade edilebiliyorsa, bu durum dummy değişken tuzağına neden olur.
    - Çözümü ise **drop_first = True** yapılarak ilk sınıf drop edilir ve değişkenlerin birbiri üzerinden oluşması(bağımlılı) engellenir.
    - get_dummies() fonksiyonu ile one-hot encoding oluşturulur.

### Rare Encoding

Rare encoding, nadir görülen kategorik değerleri bir araya getirerek, veri setindeki dengesizlikleri azaltmak için kullanılan bir kodlama tekniğidir. Bu yöntem, özellikle kategorik değişkenlerin birçok farklı değer içerdiği durumlarda kullanılır.

Rare encoding aşağıdaki adımlarla gerçekleştirilir:

1. **Kategorik Değer Frekanslarına Bakma:** Öncelikle, kategorik değişkenin değerlerinin frekanslarını kontrol ederiz. Nadir görülen değerler tespit edilir.
2. **Nadir Görülen Değerleri Bir Araya Getirme:** Belirli bir eşiğin altında olan (örneğin, 5 kez veya daha az tekrarlanan) kategorik değerler bir "Rare" kategorisine atanır.

Rare encoding'in avantajları şunlar olabilir:

1. Veri setindeki dengesizliği azaltır.
2. Modelin nadir görülen kategorilere aşırı uyum (overfitting) yapmasını önler.

### Feature Scaling (Özellik Ölçeklendirme)

Özellik ölçeklendirme amaçları: 

1. Değişkenler arasındaki ölçüm farklılığını gidermektir. Kulanacak modellerin,değişkenlere eşit şartlar altında yaklaşmasını sağlamaktır.
2. Gradient descent kullanılan algoritmaların, train sürelerini azaltma durumudur. (Uzaklık temelli yöntemlerde yanlılığın önüne geçmektir.) (Ağaca dayalı yöntemlerde göz ardı edilebilir. )

**StandardScaler:** Klasik standartlaştırma. Ortalamayı çıkar, standart sapmaya böl. z = (x - u) / s

**RobustScaler:** Medyanı çıkar iqr'a böl (Aykırı değerlere göre daha dayanıklıdır.)

**MinMaxScaler:** Verilen 2 değer arasında değişken dönüşümü

---

## Feature Extraction (Özellik Çıkarımı)

Ham veriden değşken üretmek. 

1. Yapısal Verilerden değişken üretmek → (Elimizde zaten var olan verilerden yeni bir özellik üretmek.)
2. Yapısal Olmayan Verilerden değişken üretmek (Görüntü, ses gibi verilerden özellik üretmek.)

## Feature interactions (Özellik Etkileşimleri)