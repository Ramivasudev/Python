# Write a Python script to merge two Python dictionaries.
# D21CS104
# Rami Vasudev

d1={1:10,2:20,3:40}
d2={4:40,5:50,6:35}
d=d1.copy()
d.update(d2)
print(d)