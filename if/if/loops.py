n = 5

# 1. Right Triangle
print("1. Right Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Inverted Triangle
print("\n2. Inverted Triangle")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Pyramid
print("\n3. Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# 4. Inverted Pyramid
print("\n4. Inverted Pyramid")
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

# 5. Square
print("\n5. Square")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# 6. Number Triangle
print("\n6. Number Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 7. Same Number Triangle
print("\n7. Same Number Triangle")
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# 8. Floyd's Triangle
print("\n8. Floyd's Triangle")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 9. Alphabet Triangle
print("\n9. Alphabet Triangle")
for i in range(1, n + 1):
    ch = 65
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# 10. Diamond
print("\n10. Diamond")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)