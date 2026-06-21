import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

#selection incolumn

#print(df["Name"].to_string())

#print(df["Height"].to_string())

#print(df[["Name","Height","Weight"]].to_string())
#selection by rows 

#print(df.loc["Charizard":"Blastoise", ["Height","Weight"]])

#print(df.iloc[0:11:2 ,0:3])

#pokemon = input("enter a pokemon:")

#try:
 #   print(df.loc[pokemon])
#except KeyError:
 #   print(f"{pokemon} not found")


# filtering

#tall_pokemon =  df[df["Height"] >= 2]

#heavy_pokemon = df[df["Weight"] >= 100]

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]

print(ff_pokemon)
