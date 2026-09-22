responses = {}

polling_active = True 
while polling_active:
    name = input("\n What is your name ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False
print("\n---- Poll Result -----")

for name, response in responses.items():
    print(f"{name} would like climb {response}.")


#This project is asking user's where they would love to visit and also gives us thier pull
