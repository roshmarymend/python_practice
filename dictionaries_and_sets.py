d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 40, 'e': 50}
merged_dict = {**d1,**d2}
print("Merged dictionary:", merged_dict)
print("Sorted dictionary:", dict(sorted(merged_dict.items())))

#frequency counting
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch,0)+1
print("Frequency Distribution:", freq)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("Common Elements(Intersection): ", s1&s2)
print("Unique Elements(Symmetric Difference): ", s1^s2)
print("Merged set(Union): ", s1|s2)
print("Difference of s1 from s2: ", s1-s2)
print("Sorted set: ", sorted(s1|s2))
