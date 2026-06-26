import string
import random
password = ""
stop_time = 0
password_digits = int(input("please Enter the number of digits in the password.: " ))
while True:
    for i in range(1):
        num = random.choice(string.digits)
        small = random.choice(string.ascii_lowercase)
        big = random.choice(string.ascii_uppercase)
    for i in range(1):
        word_or_number = random.choice([num,small,big])
        stop_time = stop_time + 1
        password += word_or_number
    if (stop_time == password_digits):
        break
print(password)
print("password created")
