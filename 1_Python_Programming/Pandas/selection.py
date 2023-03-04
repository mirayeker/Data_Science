#############################################################
# Selection in Pandas
#############################################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df.drop(0, axis=0).head()

#############################################################
# Değişkeni index'e çevirmek
#############################################################
df.index = df["age"]
df.drop("age", axis=1, inplace=True)
df.head()

#############################################################
# Index'i değişkene çevirmek: 1. yol
#############################################################
df["age"] = df.index
df.head()

#############################################################
# Index'i değişkene çevirmek: 2. yol
#############################################################
df = df.reset_index()
df.head()

#############################################################
# Değişkenler Üzerinde İşlemler
#############################################################

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")

# Önemli Bir nokta:
# df["age"] -> çıktısı pandas serisi
# df[["age"]] -> çıktısı pandas dataframe'i

# Yeni bir kolon oluşturmak :
df["age2"] = df["age"] * 2
df["age3"] = df["age"] / df["age2"]
df.head()

col_names = ["age2", "age3"]
df.drop(col_names, axis=1).head()

# İstediğimiz bir ifadeyi barındıran kolonu nasıl seçebilirim?
# barındırmak istemiyorsak:  df.loc[:, ~df.columns.str.contains("age")]

df.loc[:, df.columns.str.contains("age")]

#############################################################
# iloc & loc
# iloc(integer based selection): index bilgisi vererek seçim yapar.
# loc(label based selection): label' lara göre seçim yapar.
#############################################################

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.iloc[0:3]
df.loc[0:3]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

#############################################################
# Koşullu Seçim ( Conditional Selection)
#############################################################
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[(df["age"] > 50)].head(5)
df[(df["age"] > 50)]["age"].count()

# bir koşul ve iki sutun seçmek:
df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class", "sex"]].head()

#############################################################
# Toplulaştırma ve Gruplama ( Aggregation & Grouping)
#############################################################

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)

df = sns.load_dataset("titanic")
df.head(5)

# cinsiyete göre yaş ortalaması nedir?
df.groupby("sex")["age"].mean()

# Farklı bir yol yapacak olursak:
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"],
                                                 "survived": "mean"})

# Frekanslarına da bakalım sayısal değerleri ona göre yorumlayalım

df.groupby(["sex", "embark_town", "class"]).agg(
    {"age": ["mean", "sum"],
     "survived": "mean",
     "sex": "count"})

#############################################################
# Pivot Table
#############################################################


import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head(5)
# pivot_table("neyin kesişimini görmek istiyorsun", "satırlarda ne olsun", "sutunlarda ne olsun")

df.pivot_table("survived", "sex", "embarked")

# pivot_Table'ın ön tanımlı değeri mean'dir

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

# Yeni bir senaryo: elimizdeki yaş değişkenini de kırılımda görmek istiyoruz fakat yaş değişkeni sayısal nasıl yapacağız?

# cut fonksiyonu sayısal değişkenleri kategorik değişkene dönüştürmek için çok kullanılır
# qcut -> çeyrekliklere göre böler.
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])

#############################################################
# Apply ve Lambda
#############################################################
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head(5)

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5
df.head()

# uzun yol :
for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()

# apply ve lambda ile kısa yol:

df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
# Değişiklikleri kaydetmek için:

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

df.head()

#############################################################
# Birleştirme (Join) İşlemleri
#############################################################
import pandas as pd
import numpy as np

m = np.random.randint(1, 30, size=(5, 3))

df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99
pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

#############################################################
# MErge ile birleştirme işlemleri
#############################################################

df1 = pd.DataFrame({"employees": ["mark", "johm", "dennis", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["dennis", "maria", "mark", "johm"],
                    "start_date": [2010, 209, 2014, 2019]})

df3 = pd.merge(df1, df2, on="employees")
df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]
                    })
pd.merge(df3,df4)
