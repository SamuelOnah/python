
favourite_language = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'Samuel': ['go', 'python'],
    'iyojeni': ['rust', 'c++'],
    }

for name, languages in favourite_language.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")