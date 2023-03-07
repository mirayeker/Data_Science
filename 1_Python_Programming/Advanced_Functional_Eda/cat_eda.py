############################################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
############################################################
# 1- Genel Resim
# 2- Kategorik Değişken Analizi (Analysis of  Categorical Veriables)
# 3- Sayısal Değişken Analizi (Analysis of  Numerical Veriables)
# 4- Hedef Değişken Analizi (Analysis of Target Veriable)
# 5- Korelasyon Analizi (Analysis of Correlation)

############################################################
# 1- Genel Resim
############################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()


def check_df(dataframe, head =5):
    print("########################### Shape ################################")
    print(dataframe.shape)
    print("########################### Type ################################")
    print(dataframe.dtypes)
    print("########################### Head ################################")
    print(dataframe.head(head))
    print("########################### Tail ################################")
    print(dataframe.tail(head))
    print("########################### NA ################################")
    print(dataframe.isnull().sum())
    print("########################### Quantiles ################################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]))

check_df(df)

############################################################
# 2- Kategorik Değişken Analizi 1 (Analysis of  Categorical Veriables)
############################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df["sex"].value_counts()
df["sex"].unique()
df["sex"].nunique()
df.info()
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]
df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]

def catSummary(dataFrame, col_name, plot=False):
    print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(),
                        "Ratio": 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataFrame[col_name], data=dataFrame)
        plt.show(block=True)

catSummary(df, "sex", plot=True)

############################################################
# 2- Kategorik Değişken Analizi 2 (Analysis of  Categorical Veriables)
############################################################
# Eğer tipi bool ise tipini dğeiştirim görselleştirecek, kod karmaşıklaştı.
# One do thing
def catSummary(dataFrame, col_name, plot=False):
    if dataFrame[col_name].dtypes == "bool":
        dataFrame[col_name] = dataFrame[col_name].astype(int)
        print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(),
                            "Ratio": 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[col_name], data=dataFrame)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(),
                            "Ratio": 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[col_name], data=dataFrame)
            plt.show(block=True)


catSummary(df, "sex", plot=True)

############################################################
# 3- Sayısal Değişken Analizi (Analysis of  Numerical Veriables)
############################################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
print(df.head())

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]
num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

num_cols = [col for col in num_cols if col not in cat_cols]


def numSummary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)



numSummary(df, "age", plot=True)

for col in num_cols:
    numSummary(df, col)

# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi (Capturing Veraibles and Generalizing  Operations)

def grab_col_names(dataframe, cat_th=10, car_th=30):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri
    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi
    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    """

    cat_cols = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

grab_col_names(df)

def catSummary(dataFrame, col_name, plot=False):
    if dataFrame[col_name].dtypes == "bool":
        dataFrame[col_name] = dataFrame[col_name].astype(int)
        print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(),
                            "Ratio": 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[col_name], data=dataFrame)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataFrame[col_name].value_counts(),
                            "Ratio": 100 * dataFrame[col_name].value_counts() / len(dataFrame)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataFrame[col_name], data=dataFrame)
            plt.show(block=True)

for col in cat_cols:
    catSummary(df, col)


def numSummary(dataframe, numericalCol, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numericalCol].describe(quantiles).T)

    if plot:
        dataframe[numericalCol].hist()
        plt.xlabel(numericalCol)
        plt.title(numericalCol)
        plt.show(block=True)


for col in num_cols:
    numSummary(df, col, plot=True)

# BONUS
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def catSummary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    catSummary(df, col, plot=True)

for col in num_cols:
    numSummary(df, col, plot=True)



############################################################
# 4- Hedef Değişken Analizi (Analysis of Target Veriable)
############################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def grab_col_names(dataframe, cat_th=10, car_th=30):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri
    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi
    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    """

    cat_cols = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car
cat_cols, num_cols, cat_but_car = grab_col_names(df)


############################################################
# Hedef Değişkenin Kategorik Değişkenler ile Analizi
############################################################

#df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

target_summary_with_cat(df, "survived", "pclass")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)
    print("##########################################")

############################################################
# Hedef Değişkenin Sayısal Değişkenler ile Analizi
############################################################
df.groupby("survived")["age"].mean()


def target_summary_with_num(dataframe, target, numerica_col):
    print(dataframe.groupby(target).agg({numerica_col: "mean"}), end="\n\n\n")

for col in num_cols:
    target_summary_with_num(df, "survived", col)


############################################################
# 5- Korelasyon Analizi (Analysis of Correlation)
############################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv("1_Python_Programming/Advanced_Functional_Eda/breast_cancer.csv")

df.iloc[:, 1:-1]
df.head()


