height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("you are tall enough to ride!")
else:
    print("you will be able to ride when your a little older")

number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even. ")
else:
    print(f"\nThe number {number} is odd. ")