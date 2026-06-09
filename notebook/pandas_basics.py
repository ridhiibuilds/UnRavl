import pandas as pd

print(pd.__version__)
#series in pandas is a 1d labeled array that can hold any data type

df = pd.DataFrame({
    "item": ["shirt", "tshirt", "socks", "hanki", "skirt", "jeans"],
    "price": [300, 400, 150, 100, 400, 1000],
    "times_worn": [5,3,4,5,1,5]
})

print(df)
print("the most expensive item costs ",df["price"].max())
print("the cheapest item costs ",df["price"].min())

#learning filtering

print(df[df["times_worn"] == df["times_worn"].max()])

#stuff like this In UnRavl this becomes: "Show me all garments the user is most bored of" 