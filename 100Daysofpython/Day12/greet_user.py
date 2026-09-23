def greet_user(names):

    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
        
usernames = ['hannah', 'onah', 'samuel', 'Godwin']
greet_user(usernames)