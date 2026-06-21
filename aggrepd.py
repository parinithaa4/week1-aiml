import pandas as pd
df = pd.read_csv("data.csv")

#print(df.mean(numeric_only=True))

#print(df.sum(numeric_only=True))

#print(df.max(numeric_only=True))
#print(df.count())



#print(df["Height"].mean())

#print(df["Weight"].sum())

#print(df.max(numeric_only=True))
#print(df.count())

#group = df.groupby("Type1")

#print(group["Height"].count())

#df = df.drop(columns=["Legendary","No"])

#df = df.dropna(subset=["Type2"])
#df = df.fillna({
  #  "Type2":"None"
#})

#df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                 "Fire":"FIRE",
#                                "Water":"WATER"
#                               })
#df["Name"] = df["Name"].str.lower()

#df["Legendary"] = df["Legendary"].astype(bool)

df= df.drop_duplicates()
print(df.to_string())

