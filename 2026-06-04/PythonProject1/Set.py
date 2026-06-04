# Set creation
cities = {"Hyderabad", "Mumbai", "Delhi"}   # Set

print(cities)

# Duplicate values are automatically removed
cities = {"Hyderabad", "Mumbai", "Delhi", "Mumbai"}

print(cities)

# Remove duplicates from list
# cities = ["Hyderabad", "Mumbai", "Mumbai", "Delhi"]
# unique_cities = set(cities)
# print(unique_cities)

# Add single element
cities.add("Chennai")
print(cities)

# Add multiple elements
cities.update(["Delhi", "Pune"])
print(cities)

# Remove element
cities.remove("Mumbai")
print(cities)

# discard() does not give error if item is absent
cities.discard("Pune")
print(cities)