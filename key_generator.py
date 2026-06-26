import string
import random
b = 0
while True:
    for i in range(1):
        num = random.choice(string.digits)
        sma = random.choice(string.ascii_lowercase)
        bi = random.choice(string.ascii_uppercase)
    for i in range(1):
        a = random.choice([num,sma,bi])
        b = b + 1
        print(a)
    if (b == 8):
        break

