import pandas as pd

#series 

#data = [100,102,104]
#series = pd.Series(data,index=["a",'b',"c"])

#print(series[series < 103])

#calories = {"day 1": 1655,"day 2":1523, "day 3":1312}

#series = pd.Series(calories)
#print(series.loc["day 2"])

# dataframes

data = {
    "name":["sam","patrick","squid"],
    "age":[30,23,34]
}

df = pd.DataFrame(data,index=["employee1","employee2","employee3"])

df["job"] = ["cook","n/a","cashier"] # column

new_row = pd.DataFrame([{"name":"sandy","age":27,"job":"engineer"}], 
    index=["employee4"])

df = pd.concat([df, new_row])


print(df)