# Program to input from user and validate

while True:
    num = float(input("Enter a number: "))
    if -9999 < num < 9999:
        print("valid")
        break
    else:
        print("Enter a number between -9999 and 9999")
