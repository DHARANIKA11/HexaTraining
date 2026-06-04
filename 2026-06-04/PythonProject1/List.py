cities = ["Hyderabad", "Banglore", "Delhi", "Chennai"]

print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

#Negative Indexing
print(cities[-1])
print(cities[-2])

#Update an element
cities[1] = "Bengaluru"
print(cities[1])

#Adding
cities.append("Mumbai")
print(cities)

#insert
cities.insert(1, "korea")
print(cities)

#multiple value
cities.extend(["kerala","Istanbul"])
print(cities)

#remove
cities.remove("kerala")
print(cities)

cities = ["Hyderabad", "Mumbai", "Delhi"]

cities.pop(1)
print(cities)

del cities[0]
print(cities)

print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Pune" in cities)


cities.sort()
print(cities)

