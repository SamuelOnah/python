# stores information about a pizza beign oredered 
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza with the followinig toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")