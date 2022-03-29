string = [45, 6, 0, 0, 9, 89, 0, 78, 67, 56, 0, 0, 45]
for i in range(len(string)):
    string.append(string.pop(string.index(0)))
print(string)

for i  in range(len(string)):
    string.remove(0)
print(string)