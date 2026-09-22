unconfirmed_user = ['alice', 'brain', 'candace']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print(f"Verifying User : {current_user.title()}")
    confirmed_user.append(current_user)

print("\n The following user have been confirmed:")
for confirmed_user in confirmed_user:
    print(confirmed_user)