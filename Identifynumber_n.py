while True:
  try:
    Num = float(input("Enter any number. "))
    while Num <= -9999 or Num >= 9999:
      Num = float(input("Enter a new number between -9999 and 9999. "))
    print("you have chosen a valid number. ")
    break
  except ValueError:
    print("The value you entered is not a number.")
