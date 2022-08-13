import random 

up_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '"', '?', '/', '.']

print("_____________LET's CREATE YOUR NEW FB PASSWORD_____________")

enter_up_letters = int(input("How many upper cases would you like in your password? \n"))
enter_low_letters = int(input("How many lower cases would you like in your password? \n"))
enter_numbers = int(input("How many numbers would you like in your password? \n"))
enter_symbols = int(input("How many symbols would you like in your password? \n"))

print("__________________________________________________________________________\n")

password_list = []

pwd = enter_low_letters + enter_up_letters + enter_numbers + enter_symbols

for up_chars in range(1, enter_up_letters + 1):
    password_list.append(random.choice(up_letters))

for low_chars in range(1, enter_low_letters + 1):
    password_list.append(random.choice(low_letters))

for num in range(1, enter_numbers + 1):
    password_list.append(random.choice(numbers))

for symb in range(1, enter_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for up_char in password_list:
    password += up_char

if pwd == 4:
    print("Be Carefull!!! Your Password must be weak!!!")
else:
    print("NO PROBLEM!!!\n")

print("____________Here you go____________\n")
print(f"Your new fb password is {password}")