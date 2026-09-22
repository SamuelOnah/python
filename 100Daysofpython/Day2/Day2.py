# ask the user for name and age 

name = input("Whats your name? ")
age = input("How old are you? ")


print("Hello ", name + "!", "You are", age, "years old.")
# convert age to number and calculate future age 
age_number = int(age)
future_age = age_number + 10
print("In 10 year, you'll be", future_age, "years old")