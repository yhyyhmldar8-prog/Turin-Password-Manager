import string
import random
password = ""
b = 0
c = int(input("تعداد رمز مورد نیازتو وارد کن: " ))
while True:
    for i in range(1):
        num = random.choice(string.digits)
        sma = random.choice(string.ascii_lowercase)
        bi = random.choice(string.ascii_uppercase)
    for i in range(1):
        a = random.choice([num,sma,bi])
        b = b + 1
        password += a
    if (b == c):
        break
print(password)
***passworsdjjsjdjjsjdjs


***
