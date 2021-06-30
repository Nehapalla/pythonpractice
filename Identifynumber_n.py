while True:
  try:
    Num = int(input("Enter any number. "))
    while Num <= -9999 or Num >= 9999:
      Num = int(input("Enter a new number between -9999 and 9999. "))
    print("you have chosen a valid number. ")
    break
  except ValueError:
    print("The value you entered is not a number.")

if Num >= 0:
  print("The number you have chose is a positive number. ")
else:
  print("The number you have chose is a negative number. ")

if Num % 2 == 0 :
  print("You chose an even number.")
else:
  print("You chose an odd number.")

if Num > 1:
  for i in range (2,Num):
    if (Num % i) == 0:
      print(Num, "is not a prime number. " )
      break
  else:
    print(Num, "is a prime number. " )
else:
  print(Num, "is not a prime number. " )
