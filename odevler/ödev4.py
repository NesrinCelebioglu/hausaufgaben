import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#görev 1#
#soru 1#
import pandas as pd

df = pd.read_csv('customers.csv')
df.head(30)
#soru 2#
df["PLATFORM"].unique()
df["PLATFORM"].nunique()
df["PLATFORM"].value_counts()
#soru 3#
df[("PRICE")].unique()
df["PRICE"].nunique()
#soru 4#
df["PRICE"].value_counts()
#soru 5#
df["REGION"].value_counts()
#soru 6#
df.groupby("REGION")["PRICE"].sum()
#soru 7#
df.groupby("PLATFORM")["PRICE"].count()
#soru 8#
df.groupby("REGION")["PRICE"].mean()
#soru 9#
df.groupby("PLATFORM")["PRICE"].mean()
#soru 10#
df.groupby(["REGION", "PLATFORM"])["PRICE"].mean()

#görev 2#
df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"])["PRICE"].mean()

#görev 3#
df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"]).agg({"PRICE": "mean"}).sort_values('PRICE', ascending=False)
agg_df = df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE",
                                                                                                ascending=False)
agg_df.head()
#görev 4#
agg_df.index
agg_df.reset_index().head()
agg_df = agg_df.reset_index()
agg_df.head()

#görev 5#
agg_df["AGE CAT"] = pd.cut(agg_df["AGE"], bins=[0, 18, 23, 30, 40, 70],
                           labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
agg_df.tail()

#görev 6#
agg_df["customers_profile"] = [val[0].upper() + "_" + val[1].upper() + "_" + val[2].upper() + "_" + val[5] for val in
                               agg_df.values]
agg_df["customers_profile"].head()
agg_df = agg_df.groupby("customers_profile").agg({"PRICE": "mean"}).sort_values('PRICE', ascending=False)
agg_df = agg_df.reset_index()
agg_df.sort_values("customers_profile", ascending=False)
agg_df.head()

#görev 7#
agg_df["SEGMENT"] = pd.cut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

#görev 8#
new_customer = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_profile"] == new_customer]
new_customer = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_profile"] == new_customer]


