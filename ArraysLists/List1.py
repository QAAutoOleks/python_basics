import random

nums = []
print(nums)
for i in range(10):
    nums.append(random.randrange(1, 11))

nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

new_list = list()  # list() - list constructor used to create new list
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(new_list)

nums2 = [1, 2, [100, 200, 300], 3, True, "Text", 9, 11] # list include list
print(nums2[2][0]) # зверенння до листа в листі
print(nums2[2][-1])
