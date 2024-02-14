"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Foniok
email: karel.foniok@gmail.com
discord: karel_10181
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]


# Program si vyžádá od uživatele přihlašovací jméno a heslo a 
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
username = input("Username: ")
password = input("Password: ")


# pokud je registrovaný a zadá správné heslo, pozdrav jej a umožni mu analyzovat texty
if username in users:
    passwords = passwords[users.index(username)]

    if passwords == password:
        print("-" * 40)
        print(f"Welcome to the app, {username} \nWe have 3 texts to be analyzed.")
        print("-" * 40)

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
        text_selection = input("Enter a number btw. 1 and 3 to select: ")

# Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.    
        if text_selection.isnumeric() is False:
            print("Not a number....terminating program")

# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
        elif int(text_selection) not in range(1,4):
            print("Selection not in required range......terminating program")

# Pokud je vše v pořádku, proběhne výběr textu
        else:
            text = TEXTS[int(text_selection)-1]
            
            print("-" * 40)

# Pro vybraný text spočítá počet slov:
            slova = list()
            for slovo in text.split():
                slova.append(slovo.strip(",.;:"))
            
            titlecase = 0
            uppercase = 0
            lowercase = 0
            numeric = 0
            sum_of_numbers = 0

            
            for word in slova:

# počet slov začínajících velkým písmenem
                if word[0].isupper():
                    titlecase += 1
            
# počet slov psaných velkými písmeny,            
                elif word.isupper():
                    uppercase += 1
           
# počet slov psaných malými písmeny,           
                elif word.islower():
                    lowercase += 1
             
# počet čísel a sumu všech čísel v textu             
                elif word.isnumeric():
                    numeric += 1
                    sum_of_numbers += int(word)
           
    
            print(f"There are {len(slova)} words in the selected text.")
            print(f"There are {titlecase} titlecase words.")
            print(f"There are {uppercase} uppercase words.")
            print(f"There are {lowercase} lowercase words.")
            print(f"There are {numeric} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")

            print("-" * 40)

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.                       
            delka_slov = dict()

            for word in slova:
                if len(word) not in delka_slov:
                    delka_slov[len(word)] = 1
                else:
                    delka_slov[len(word)] += 1

            delka_slov_list = list(delka_slov.keys())
            delka_slov_list.sort()
            sorted_delka_slov = {i: delka_slov[i] for i in delka_slov_list}

            print("LEN| OCCURENCES", " " * ((max(delka_slov.values()))-12), "|NR")
            print("-" * 40)

            for key in sorted_delka_slov:
                print(" " * (2 - len(str(key))), key, end="")
                print("|", "*" * sorted_delka_slov[key], end="")
                print((max(delka_slov.values())-sorted_delka_slov[key]) * " ", sorted_delka_slov[key], sep="|")

# pokud je uživatel registrovaný, ale zadá špatné heslo, sděl mu tuto informaci
    else:
        print(f"You input wrong password, {username}")

# pokud uživatel není registrovaný, upozorni jej a ukonči program.
else:
    print("Unregistered user, terminating the program.")