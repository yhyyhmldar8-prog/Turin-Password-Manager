import string
import random
password = ""
stop_time = 0
stop_time1 = 0
stop_time2 = 0
while True:
    for i in range(1):
        num = random.choice(string.digits)
        small = random.choice(string.ascii_lowercase)
        big = random.choice(string.ascii_uppercase)
    for i in range(1):
        word_or_number = random.choice([num,small,big])
        stop_time = stop_time + 1
        password += word_or_number
    if (stop_time == 8):
            break
print(password)
print("password created")
password1 = ""
choice = input("do you want choose password digits number?: ")
if choice == "yes":
    choice2 = input("do you want sepcial symbol in your password?(yes/no):\n ")
    if choice2 == "yes":
        password_digits = int(input("please Enter the number of digits in the password.: " ))
        while True:
            for i in range(1):
                spec1 = random.choice(string.punctuation)
                num1 = random.choice(string.digits)
                small1 = random.choice(string.ascii_lowercase)
                big1 = random.choice(string.ascii_uppercase)
            for i in range(1):
                word_or_number1 = random.choice([num1,small1,big1,spec1])
                stop_time1 = stop_time1 + 1
                password1 += word_or_number1
            if (stop_time1 == password_digits):
                break
    elif choice2 == "no":
        password_digits = int(input("please Enter the number of digits in the password.: " ))
        while True:
            for i in range(1):
                num2 = random.choice(string.digits)
                small2 = random.choice(string.ascii_lowercase)
                big2 = random.choice(string.ascii_uppercase)
                word_or_number2 = random.choice([num2,small2,big2,])
                stop_time2 = stop_time2 + 1
                password1 += word_or_number2
            if (stop_time2 == password_digits):
                break
        print(password)
        print("password created")
    else :
        print("please only write yes or no")
elif choice == "no": 
 print("good bye")
else :
    print("please only write yes or no")
print(password1)
print("password created")
