while True:
  try:
    Num = float(input("Enter any number. "))
  except ValueError:
    print("You have chosen an invalid number. Enter a new number between -9999 and 9999.")
    continue
  while Num < -9999 or Num > 9999:
    Num = float(input("Enter a new number between -9999 and 9999. "))
  print("You have chosen a valid number. ")
  
