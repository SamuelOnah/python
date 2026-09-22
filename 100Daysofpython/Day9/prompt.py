message = input("Tell me something, and i will repeat it back to you: ")
print(message)

name = input("please enter your name: ")
print("Hello",name, "!")

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)