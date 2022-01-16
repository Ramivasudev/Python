# Write a Python script to concatenate the following dictionaries to create a new one.
# D21CS104
# Rami Vasudev

d1={1:20,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
t={}
for val in (d1,d2,d3):
    t.update(val)
print(t)
