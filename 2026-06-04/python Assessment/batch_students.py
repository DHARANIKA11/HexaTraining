batch_a = {
"Rahul",
"Priya",
"Amit",
"Sneha",
"Farhan"
}
batch_b = {
"Priya",
"Sneha",
"Neha",
"Arjun",
"Farhan"
}

batch_a = {"Rahul", "Priya", "Amit", "Sneha", "Farhan"}
batch_b = {"Priya", "Sneha", "Neha", "Arjun", "Farhan"}

print("\n Common Students:", batch_a.intersection(batch_b))

print("Only in Batch A:", batch_a - batch_b)

print("Only in Batch B:", batch_b - batch_a)

print("All Unique Students:", batch_a.union(batch_b))

print("Present in One Batch Only:", batch_a.symmetric_difference(batch_b))

