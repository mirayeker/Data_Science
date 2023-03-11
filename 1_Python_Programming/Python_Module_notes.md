# Python Programming for Data Science

---

## STRING METHODS

```python
dir(str)

len("MirayEker")

###############################################
# upper() & lower() : buyuk kücük dönüşümleri
###############################################

"mirayeker".upper()
"MIRAYEKER".lower()

###############################################
# replace(): karakter değiştirir
###############################################

hi= "hello AI Era"
hi.replace("l","k")

###############################################
# split(): böler
###############################################

"Hello AI ERA".split()

###############################################
# strip(): kırpar (önden arkadan)
###############################################

"!!Hello AI ERA!!".strip("!")

###############################################
# capitalize(): ilk harfi büyütür
###############################################

"miray eker".capitalize()

###############################################
# join(iter): iterasyon yapılabilecek yapıya ekleme yapar !!itersyon yapısı string olmalı!!
###############################################

"--".join(['python', 'is', 'cool'])

".".join(["1","2","3","4"])
```

## LIST METHODS

 

```python
#######################################
# Liste
#######################################

# - Değiştirilebilir
# - Sıralıdır. İndex işlemleri yapılabilir.
# - Kapsayıcıdır. (yani liste elemanları diğer veri yapılarını içerebilir.

notes = [1,2,3,4,5]
type(notes)

#######################################
# slice işlemi:
#######################################

notes[0:3]

#######################################
# Liste metodları (list methods)
#######################################
dir(notes)
len(notes)

#######################################
# append: eleman ekler
#######################################
notes.append(100)
notes

#######################################
# pop : index'e göre eleman siler
#######################################

notes.pop(0)
notes

#######################################
# insert :  index'e ekler
#######################################

notes.insert(2,"Miray")
notes
```

## DICTIONARY METHODS

```python
#######################################
# Dictionary
#######################################

# - Değiştirilebilir
# - Sırasızdır. (3.7 sürümünden sonra sıralı hale gelmiştir)
# - Kapsayıcıdır.

# key - value

dict = {"REG" : ["Regression",10],
       "LOG" : ["Logistic Regression",20],
       "CART" : ["Classification and Reg",30]}

dict["CART"][1]

#######################################
# Key Sorgulama
#######################################

"REG" in dict

#######################################
# Value değiştirmek
#######################################

dict["REG"] = ["YSA",15]

#######################################
# Tüm Key'lere ve Value'ye erişmek erişmek:
#######################################

dict.keys()
dict.values()

#######################################
# Tüm çiftleri Tuple Halinde Listeye çevirme
#######################################

dict.items()

#######################################
# Key ve value değerlerini güncellemek:
#######################################

dict.update({"REG":11})

```

 

## COMPREHENSIONS

```python
#############################################
# COMPREHENSIONS
#############################################

#############################################
# List Comprehensions
#############################################

salaries = [2000, 4000, 1500, 3000, 7000]

# adım adım geliştirerek yazalım.

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary <= 3000]

[salary * 2 if salary <= 3000 else salary * 0.2 for salary in salaries]

def new_salaries(salary):
    return (salary * 2) + salary

# List comprehension yapısına fonksiyon  ekledik.

[new_salaries(salary * 2) if salary <= 3000 else new_salaries(salary * 0.2) for salary in salaries]

# hadi şimdi bunu kaydedelim

yeniMaas = [new_salaries(salary * 2) if salary <= 3000 else new_salaries(salary * 0.2) for salary in salaries]
yeniMaas

#############################################
# -yeni bir senaryo kuralım
# - aşağıda verilen öğrenci listelerinden istenmeyen öğrencilerin ismini küçük diğerlerini büyük yazdıralım
#############################################
students = ["Mark", "Sude", "Jhon", "Ali"]
students_no = ["Mark", "Jhon"]

[student.lower() if student in students_no else student.upper() for student in students]

#############################################
# Dictionary Comprehensions
#############################################

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

dictionary.keys()
dictionary.values()
dictionary.items()

# dictionary.items() -> liste formunda ama herbir elemanı tuple olarak ifade edilmiş şekilde erişmek istersek.

# adım adım geliştirerek öğrenelim:

{k: v**2 for (k,v) in dictionary.items()}

{k.upper(): v**2 for (k,v) in dictionary.items()}
```

<aside>
💡 List Comprehension, liste tanımlanması gibi yapılır içine [ if else yapıları, fonksiyon, döngü ] yapıları yazılabilir. Buradan çıkacak sonucun tek bir liste halinde çıkması beklenilir.

</aside>

<aside>
💡 list comprehension yapısında sadece bir tane if varsa en sağa yazılır if else yapsı varsa for döngüsü en sağa yazarız.

</aside>

## MÜLAKAT SORULARI

```python
######################################
#1. senaryo

# Amaç -> çift sayıların karesi alınarak bir sözlüğe eklenmek istenmiştir.
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacaktır.

######################################

numbers = range(10)

new_dict = {}

{n: n**2 for n in numbers if n % 2 == 0}

######################################
#2. senaryo

# Amaç -> bir veri setindeki Değişken isimlerini değiştirmek.

######################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]

######################################
#3. senaryo

# Amaç -> bir veri setindeki Değişken isiminde 'INS' olanların başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

######################################
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.columns = [col.upper() for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

######################################
#4. senaryo

# Amaç -> Key!i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.

######################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

####################################
# uzun yol

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

############################################

#kısa yol

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)
```

<aside>
💡 Method ve fonksiyonun birbirinden farkı: Eğer bir fonksiyon class yapısı içerisinde tanımlandıysa method’dur. Class yapısı içinde değilse fonksiyondur.(fonksiyonlar bağımsız methodlar ise classlar içerisinde tanımlanmıştır.) (yalnız ikisininde görevi aynıdır)

</aside>

## NUMPY LIBRARY

<aside>
💡 Numpy’ın listelerden farklılaştığı iki önemli nokta:

- verimli veri saklama
- yüksek seviyeden işlemler (vektörel işlemler)
</aside>

<aside>
💡 Python’un sahip olduğu gibi(list,tuple,dict..) Numpy’ın da veri yapısı vardır buna numpy array’i (ndarray) adı verilir.

- Numpy işlemleri yapabilmek için öncelikle numpy array’ine ihtiyaç vardır.
</aside>

```python
##################################
# NUMPY
##################################

##################################
# Neden Numpy:

# sabit tipte veri tutarak işlemleri daha hızlı yapar.
# vektörel seviyeden işlemler yaparak daha fazla iş daha az çaba gerektirir.

##################################
import numpy as np

a = [1,2,3,4]
b = [2,3,4,5]

# iki listeyi çarpmak istersek (numpy'sız) :
ab = []

for i in range(0,len(a)):
    ab.append(a[i] * b[i])
ab
#numpy ile high seviyede hemen halledebiliriz:

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

##################################
#Numpy Array'i Oluşturmak (Creating Numpy Arrays)

# Python’un sahip olduğu gibi(list,tuple,dict..),
# Numpy’ın da veri yapısı vardır buna numpy array’i adı verilir.
# Numpy işlemleri yapabilmek için öncelikle numpy array’ine ihtiyaç vardır.
##################################

import numpy as np

np.array([1, 2, 3, 4])
type(np.array([1, 2, 3, 4]))

np.zeros(10,dtype=int) # 10 tane sıfırdan oluşan int np array'i
np.random.randint(0, 10, size=10) # 0 - 10 arasında 10 elemanı olan np array'i
np.random.normal(10, 4, (3,4)) # ortalaması 10 standart sapması 4 olan 3'e 4'lük bir np array'i oluşturduk

##################################
#Numpy Array  Özellikleri (Attributes of Numpy Arrays)

# ndim :  boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

##################################
import numpy as np
a = np.random.randint(10, size = 5)
a.ndim
a.shape
a.size
a.dtype

##################################
# Yeniden Şekillendirme (Reshaping)
##################################

import numpy as np

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3) # dikkat edilmesi gereken husus: 3x3 = 9 elemanlı bir matrix oluşturabiliriz ( eleman sayılarına dikkat)

##################################
# Index Seçimi (Index Selection)
##################################

import numpy as np

a = np.random.randint(10, size=10)
a[0]
a[1:5] #sciling
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0] = 88.4 # tek tip veri tuttugu için 88 olarak gösterir. (fix type )

m[:, 0]  #sciling işlemi:  tum satırları sec yalnızca 0. sütunu sec
m[0:2, 1:3]
m[1, :]

##################################
# Fancy Index

# fancy index işlemi ile elimizde bulunan index listesini np arrayine vererek birden fazla index seçimi yapabiliriz
##################################
import numpy as np

v = np.arange(0, 30, 3)  # (0'dan 30'a kadar 3'er 3'er giderek array oluştur)

catch = [2, 4, 6]

v[catch]

##################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy )

##################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

# senaryo: değeri 3'den küçük olanlara erişelim.

# Klasik Döngü ile :
ab = []

for i in v:
    if i < 3:
        ab.append(i)
ab

# Numpy ile :
# v [buraya index bilgisi barındıran liste girebiliyoruz, true false ifadelerinden oluşan bir array'de gönderebilirz.]

v < 3 #  array([ True,  True, False, False, False]) tüm elemanları dolandı ve songuya göre true false döndürdü

v[v < 3]

#diğer senaryolara göre
v[v > 3]
v[v != 3]

##################################
# Matematiksel İşlemler ( Mathematical Operations )

##################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2

v= np.subtract(v, 1)
np.add(v, 3)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
```

## PANDAS LIBRARY

<aside>
💡 Pandas Series’ler genellikle veri manipülasyonu ve veri analizlerinde kullanılır.

- pandas seri'leri index bilgisi barındıran tek boyutlu veri tipidir.
- pandas dateframe ise index bilgisi barındıran çok boyutlu veri tipidir.
</aside>

<aside>
💡 pandas’da çalışırken karşılaşabileceğimiz object ve category değişken kategorik değişkendir.

- Aralarında bir fark var mıdır? fonksiyonla birlikte kullanırken vardır ama biz ikisini de kategorik değişken olarak ele alacağız.
</aside>

<aside>
💡 df.describe().T diyerek betimsel istatistik bilgilerine eriştik.

- count: kaç gözlemden oluştuğu
- mean : ortlamasını
- std : standart sapmasını
- %25, %50, %75 : çeyrekliklerini ifade eder
- df[”column_name”].value_count() → seçilen kategorik değişkende kaç sınıf ve sınıfın kaç elemanı var bilgisine erişebiliriz.
</aside>

<aside>
💡 iloc(integer based selection) & loc(label based selection)

- iloc: Index’e göre seçim yapar.
- loc: Label’e göre seçim yapar.
</aside>

<aside>
💡 Pivot table:

- groupby işlemlerine benzer şekilde veri setini kırılımlar açısından değerlendirmek ve ilgilendiğiimiz özet istatistiği bu kırılımlar açısından görme imkanı sağlar.
- `df.pivot_table("survived", "sex", "embarked")` kesişimlerde neyi görmek istiyorsun: “survived”, satırda hagi değişkeni görmek istiyorsun:”sex” sütunda hangi değişkeni görmek istiyorsun: “embarked”
- pivot_Table’in ön tanımlı değeri: “mean”’dir. Girilen değişkenlerin ortalamasını verir.
</aside>

<aside>
📌 pd.cut() ve pd.qcut() fonksiyonları elimizdeki sayısal değişkenleri kategorik değişkenlere çevirmek için kullanılan en yaygın fonksiyonlardır.

```python
pd.cut(df["age"], [0, 10, 18, 25, 40, 90],
                       labels=["cocuk", "genc", "yetiskin", "orta_yasli", "yasli"])
```

</aside>

```python
##################################
# PANDAS
##################################

##################################
# Pandas Series
# pandas seri'leri index bilgisi barındıran tek boyutlu veri tipidir.
# pandas dateframe ise index bilgisi barındıran çok boyutlu veri tipidir.
##################################

import pandas as pd

s = pd.Series([10, 20, 33, 45, 87])
#Series bir metot'dur. içine girilen tipi, seriye dönüştürür. (index bilgileri iç özelliktir.)
type(s)
s.index
s.dtype
s.ndim
s.size

s.values
type(s.values) # dikkat s.values dediğimizde indexler ile ilgilenmiyoruz dediğimiz için numpy ndarry döndüğünü unutmayalım.

s.head()
s.tail()

##################################
# Veri Okuma (reading Data)
##################################

import pandas as pd

df = pd.read_csv("hafta_2/datasets/advertising.csv")
df.head(5)

##################################
# Veri'ye Hızlı Bir Bakış ( Quick Look at Data)
##################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape

df.info() # veri setiyle ilgili özet bir bilgi vermektedir.
df.columns # veri setinde bulunan tüm değişkenlerin isimlerine erişebiliriz.

df.index

df.describe().T # Özet istatistik bilgilerine erişmek için kullanıyoruz.  .T diyerek daha okunabilir anlaşılabilir hale geliyor.

df.isnull().values.any() # veri setinde eksiklik var mı?
df.isnull().sum() #hangi değişkende ne kadar var?

# senaryo: herhangi bir kategorik değişkenin kaç tane sınıfı ve sınıfların kaç elemanı var dersek:

df["sex"].value_counts()

##################################
# Pandas'ta Seçim İşlemleri ( Selection in Pandas)
##################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]

df.drop(0, axis=0).head()

delete_indexs=[1, 3, 5, 7]
df.drop(delete_indexs, axis=0).head(10)

#Kalıcı şekilde kaydetmek için 2 yol

#df = df.drop(delete_indexs, axis=0).head(10) #1. yol
# df.drop(delete_indexs, axis=0, inplace=True) #2. yol !! dikkat çoğu metotda kalıcı değişiklik yapmak içn,
# genelde inplace=True argümanı kullanılır.

##################################
# Değişkeni Index'e Çevirmek
# senaryo: yaş değişkenini index olarak kullanalım ve yas değişkenini sütundan kaldıralım:
##################################

df["age"].head()
df.age.head()

df.index=df["age"]
df.drop("age", axis=1).head()
df.drop("age", axis=1, inplace=True)

##################################
# Index'i Değişkene Çevirmek
##################################
#1. yol
df.index
df["age"] = df.index
df.head()

#df.drop("age", axis=1, inplace=True)
#2. yol

df.reset_index().head() #indexteki değişkeni sütun'a çevirir ve index'i sıralar
df.head()

##################################
# Değişkenler Üzerinde İşlemler
##################################

import pandas as pd
import seaborn as sns
#pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()
type(df["age"]) #PANDAS SERIES çıktıı!!!!  eğer data frame olarak çıkasını istiyorsak:
type(df[["age"]]) #çift köşeli parantez şeklinde yazarız.

df[["age", "alive"]]

col_names= ["age", "adult_male", "alive"]
df[col_names] # birden fazla değişkene ulaşmak istediğimizde

df["age2"] = df["age"] ** 2 #yeni bir değişken oluşturduk.
df["age3"] = df["age"] * 2
df

df.drop("age2", axis=1)

#Önemli bir şey:
df.loc[:, ~df.columns.str.contains("age")].head()

##################################
# iloc & loc
##################################
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# iloc (integer based selection)
df.iloc[0:3]
df.iloc[0, 0]

#loc (label based selection)
df.loc[0:3]

#aradaki farkı gözlemleyelim

df.iloc[0:3, 0:3]
df.loc[0:3, "age"]
####################

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

##################################
# Koşullu Seçim İşlemleri (conditional Selection)
##################################

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, "class"].head()
df.loc[df["age"] > 50, ["age", "class"]].head()

#birden fazla koşul girelim:
df.loc[(df["age"] > 50) & (df["sex"] =="male"), ["age", "class"]].head()
df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) &
       (df["sex"] =="male") &
       ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]].head()
df["embark_town"].value_counts()

##################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
##################################

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# yaş ve cinsiyet ile ilgili senaryo: kadınların ve erkeklerin yaş ortalamasına erişelim dersek:

df["age"].mean()

df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age": "mean"}) # bu kullanım daha kullanışlı
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})

##################################
# Pivot Table
##################################

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

# senaryo: yaş değişkeni bu kırılıma nasıl etki etmiş,

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90],
                       labels=["cocuk", "genc", "yetiskin", "orta_yasli", "yasli"]) # burada sınırları belirledik peki ya bunlara bir isim vermek isteseydik??

df.pivot_table("survived", "sex", "new_age")
df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option("display.width", 550) #çıktıları yan yana görebilmek içi bir ayar yaptık.

##################################
# Apply & Lambda
#- Apply, satır ya da sütunlarda istediğimiz fonksiyonları uygulayabiliriz.
# Lambda, bir fonksiyon tanımlama şeklidir normal fonksiyonlardan farkı  kullan-at fonksiyonudur.
# Tanımlamadan fonksiyon kullanma fırsatı verir.
##################################
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

## uzun yol ##
for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()

## kısa yol ( birkaç farklı senaryo üzerinden)

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean())/ x.std()).head()

def standar_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()
df.loc[:, df.columns.str.contains("age")].apply(standar_scaler).head()

##################################
#Birleştirme (Join) İşlemleri
##################################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, (5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])
pd.concat([df1, df2], ignore_index=True)

##################################
#Merge ile Birleştirme İşlemi
##################################
df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})
pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

#senaryo: Her çalışanın müdür bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting",  "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4)
```