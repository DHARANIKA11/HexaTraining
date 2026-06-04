# Set creation
set1 = {"Python", "SQL"}

set2 = {"MongoDB", "Python"}

# Union
result = set1.union(set2)
print("Union:", result)

# Intersection
result = set1.intersection(set2)
print("Intersection:", result)

# Difference
result = set1.difference(set2)
print("Difference (set 1):", result)

result = set2.difference(set1)
print("Difference (set 2):", result)

# Symmetric Difference (Non-common values)
result = set1.symmetric_difference(set2)
print("Symmetric Difference:", result)