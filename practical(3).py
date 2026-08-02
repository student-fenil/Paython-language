text = input("Enter words: ")

words = text.split()

unique = []

for w in words:
    if w not in unique:
        unique.append(w)

print("After removing duplicates:")
print(" ".join(unique))
##################################################

list=[1,2,3]
print(list)
list[2]=9
print(list)
