import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","<",">","$","&","%","^","*"]


letter_need = int(input("Enter the number of letters you need in your password : \n"))
number_need = int(input("Enter the number of number you need in your password : \n"))
symbol_need = int(input("Enter the number of symbols you need in your password : \n"))


password = []
for i in range(0,letter_need):
    password.append(random.choice(letters))

for i in range(0,number_need):
    password.append(random.choice(numbers))

for i in range(0,symbol_need):
    password.append(random.choice(symbols))

random.shuffle(password)


passwords = ""

for char in password:
    passwords += char
print(passwords)