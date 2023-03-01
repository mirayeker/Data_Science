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
#df["age"] -> çıktısı pandas serisi
#df[["age"]] -> çıktısı pandas dataframe'i

# Yeni bir kolon oluşturmak :
df["age2"] = df["age"] * 2
df["age3"] = df["age"] / df["age2"]
df.head()

col_names= ["age2", "age3"]
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


col_names = [ "age", "embarked", "alive"]
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

df.loc[ (df["age"] > 50) & (df["sex"] == "male"), ["age", "class", "sex"]].head()

