import string
import random

password = ""
stop_time = 0  # counter to track how many characters have been added
password_digits = int(input("How many digits you want the password to be? "))

while True:
    # Pick one random digit, one random lowercase letter, and one random uppercase letter
    for i in range(1):
        num = random.choice(string.digits)
        small = random.choice(string.ascii_lowercase)
        big = random.choice(string.ascii_uppercase)

    # Randomly choose ONE of the three (num, small, big) and append it to the password
    for i in range(1):
        word_or_number = random.choice([num, small, big])
        stop_time = stop_time + 1
        password += word_or_number

    # Stop once the password has reached the desired length
    if stop_time == password_digits:
        break

print(password)
print("password created")