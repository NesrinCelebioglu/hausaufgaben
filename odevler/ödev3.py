#görev1#

import seaborn as sns

df =sns.load_dataset("titanic")
df.head()

#görev2#
df["sex"].value_counts()

#görev3#
df.nunique()

#görev4#
df["pclass"].nunique()
df["pclass"].unique()

#görev5#
df[["pclass","parch"]].nunique()

#görev6#

df["embarked"].dtype
df.info()

df["embarked"].astype("category")

#görev7#
df[df["embarked"] == "C"].head(20)

#görev8#
df[df["embarked"] != "S"].head(20)

#görev9#
df.loc[(df["sex"] == "female") & (df["age"] < 30)]

#görev10#
df.loc[(df["fare"] > 500) & (df["age"] >70)].head()

#görev11#

df.isnull().sum()
df.isna().sum()

#görev12#

df =sns.load_dataset("titanic")
df.drop("who", axis=1 , inplace = True)
#bu kalici degisiklik yapiyor#
xyz = df.columns.drop("sex")
print(xyz)
#bu kalici degisiklik yapmiyor#

df.columns

#görev13#
df =sns.load_dataset("titanic")
df["deck"] = df["deck"].fillna(df["deck"].mode()[0])
df["deck"]
df

#görev14#
df["age"] = df["age"].fillna(df["age"].median())
df["age"]
df

#görev15#
df =sns.load_dataset("titanic")
df.groupby(["pclass", "sex"]).agg({"survived":["sum", "count", "mean"]})

#görev16#

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

df

#görev17#

import seaborn as sns
import pandas as pd
import numpy as np
df1 =sns.load_dataset("tips")
df1.columns

#görev18#

df1.groupby(["time"]).agg({"total_bill":["sum","min","max","mean"]})

#görev19#

df1.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]})

#görev20#

df1.loc[(df1["time"] == "Lunch") & (df1["sex"]== "Female")].groupby(["day"]).agg({"total_bill":["sum","min","max"],"tip":["sum","min","max"]})


#görev21#

df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10)]

df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10)]["total_bill"].mean()


df1


#görev22#

df1["total_bill_tip_sum"] = df1["total_bill"] + df1["tip"]

df1

#görev23#

df1 = df1.sort_values("total_bill_sum", ascending=False).head(30)
df1


