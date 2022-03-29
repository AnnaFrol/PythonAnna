string = input()
a = string[:string.find('h')]
b = string[string.find('h'):string.rfind('h') + 1]
c = string[string.rfind('h') + 1:]
string = a + b[::-1] + c
print(string)