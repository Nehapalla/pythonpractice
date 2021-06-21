# Program to input from user and validate

while True:
    num = int(input("Enter number: "))
    if -9999 < num < 9999:
        print("valid")
        break
    else:
        print("Enter a number between -9999 and 9999")

