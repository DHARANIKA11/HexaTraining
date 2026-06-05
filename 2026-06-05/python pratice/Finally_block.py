# Finally Block Example

try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Connection Closed")


# Raise Error Example

salary = -1000

if salary < 0:
    raise ValueError("Salary cannot be negative")