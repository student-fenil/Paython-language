students = []

# Append names
for i in range(5):
    name = input("Enter student name: ")
    students.append(name)

print("\nStudent List:", students)

# Sorted list
print("\nSorted List:")
print(sorted(students))

# Count total students
print("\nTotal number of students:", len(students))

# Last 3 names
print("\nLast 3 names in list:")
print(students[-3:])
