dict1 = {}
print(f"Empty dictionary\n{dict1}\n")

# create using dict()
dict2 = dict({"Ukraine": "Kyiv", "UK": "London"})
print(f"Dictionary with the use of dict():\n{dict2}\n")

# print element using key and 'get' command
print(f"Print element using key 'UK':\n{dict2["UK"]}")
print(f"Print element using 'get' and key 'UK':\n{dict2.get("UK")}\n")

# command dict() will convert each pair of values
# (1, "Washington"), (2, "Paris")
# to key-value pair
dict3 = dict([(1, "Washington"), (2, "Paris")])
print(f"Dictionary with each item as a pair:\n{dict3}\n")

# add elements
dict4 = dict()
print(f"Empty 'dict4':\n{dict4}")
dict4[0] = "Sevastopol"
dict4[1] = "Hmelnytskyi"
dict4[2] = "Lutsk"
print(f"'dict4' after adding 3 elements:\n{dict4}\n")

# add set
dict4['Value_set'] = 2, 3, 4
print(f"'dict4' after adding set:\n{dict4}\n")

# update element
dict4[1] = "Poltava"
print(f"'dict4' after updating:\n{dict4}\n")