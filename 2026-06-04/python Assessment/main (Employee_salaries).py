

salaries = [45000, 55000, 65000, 75000, 85000]
print("Salaries:", salaries)

print(" Maximum Salary:", max(salaries))
print(" Minimum Salary:", min(salaries))

print("Total Salary Payout:", sum(salaries))
print("Average Salary:", sum(salaries) / len(salaries))

salaries.extend([95000, 105000])
print("After Adding Salaries:", salaries)

salaries.remove(55000)
print("After Removing 55000:", salaries)


salaries.sort()
print("Ascending Order:", salaries)


salaries.sort(reverse=True)
print(" Descending Order:", salaries)

print("Second Highest Salary:", salaries[1])

print("Salaries > 70000:")
for salary in salaries:
    if salary > 70000:
        print(salary)



