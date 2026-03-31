s1 = {"a", "b", "c"}
s2 = {1, 2, 3, "b"}

for item in s1:
    print(item)

combined = s1 | s2
common = s1 & s2
only_s1 = s1 - s2

print(combined)
print(common)
print(only_s1)