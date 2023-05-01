x = set("A Python Tutorial")
print(x)

#A list passing to a set 
x = set(["what", "How", "Why"])
print(x)

#checking by passing a tuple into set if it removes duplicates
x = set(("BZW", "HYD", "BAN", "DEL", "HYD"))
print(x)

# using difference() method using sets
s = {1,2,3,4}
d = {3,4,5,6}
e = {2,3,4,5,6}
print(s.difference(d).difference(e))

# using difference_update() method
s = {1,2,3,4}
d = {3,4,5,6}
print(s.difference_update(d))

#working with union and intersection 
s = {1,2,3,4}
d = {3,4,5,6}
print(s | d)
print(s & d)

# isdisjoint() method is used to find the difference in the set or sees they have any intersections
s = {1,2,3,4}
d = {3,4,5,6}

print(s.isdisjoint(d))

# using issubset() and issupperset() method
s = {1,2,3,4}
d = {3,4,}
print(d.issubset(s))
print(s.issuperset(d))



