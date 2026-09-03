print("Welcome to Onah Samuel Guessing Game")

secret_Number = 88
attempts = 0

while True:
    guess =  int(input("Enter your Guess"))               
    attempts += 1

    if guess > secret_Number:
        print("Too High")
    elif guess < secret_Number:
        print("Too Low")
    else:
        print("You made the correct guess")
        print("You got it in", attempts, "attempt")
        break 
print("thank you for trying out one of our games")