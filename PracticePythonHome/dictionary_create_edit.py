dict1 = {}
print(f"Empty dictionary\n{dict1}")

# create using dict()
dict2 = dict({"Ukraine": "Kyiv", "UK": "London"})
print(f"Dictionary with the use of dict():\n{dict2}")

# command dict() will convert each pair of values
# (1, "Washington"), (2, "Paris")
# to key-value pair
dict3 = dict([(1, "Washington"), (2, "Paris")])
print(f"Dictionary with each item as a pair:\n{dict3}")
