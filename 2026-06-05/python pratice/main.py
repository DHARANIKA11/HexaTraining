#a = 10
#b=0
#result = a/b
#print(result)
#print("Program completed")

file = open("employees.txt", "r")

data = file.read()

print(data)

file.close()

# Read One Line from File

file = open("employees.txt", "r")

print(file.readline())

file.close()


# Read Multiple Lines

file = open("employees.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# Automatically Close the File

with open("employees.txt", "r") as file:
    data = file.read()
    print(data)

# Write into File

with open("employees1.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")


# Append into File

with open("employees1.txt", "a") as file:
    file.write("Anit\n")