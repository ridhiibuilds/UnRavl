import pandas as pd

# print(pd.__version__)
# #series in pandas is a 1d labeled array that can hold any data type

# df = pd.DataFrame({
#     "item": ["shirt", "tshirt", "socks", "hanki", "skirt", "jeans"],
#     "price": [300, 400, 150, 100, 400, 1000],
#     "times_worn": [5,3,4,5,1,5]
# })

# print(df)
# print("the most expensive item costs ",df["price"].max())
# print("the cheapest item costs ",df["price"].min())

# #learning filtering

# print(df[df["times_worn"] == df["times_worn"].max()])

#stuff like this In UnRavl this becomes: "Show me all garments the user is most bored of" 

df = pd.read_csv("data/myntra_products_catalog.csv")
# print(df.head())
# print(df.columns)
# print(df.shape)

print(df["PrimaryColor"].nunique())
print(df["Price (INR)"].max())
#to like print the frequencies of diff items repeating ones
# print(df["Gender"].value_counts())
# print(df["ProductBrand"].value_counts())



# print(df[df["PrimaryColor"]== "Black"])
# we found out the data set we downloaded is a dirty dataset means there are some typing issues , using "Black" didnt give us result cause in the dataset it is " Black"
print(df["PrimaryColor"].value_counts().head(10))

#we can either improve the dataset or use " Black"
# print(df[df["PrimaryColor"]== " Black"])

#improving 
df["PrimaryColor"] = df["PrimaryColor"].str.strip()
print(df[df["PrimaryColor"]== "Black"])
