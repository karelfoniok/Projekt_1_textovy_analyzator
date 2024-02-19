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

separator = "-" * 40

# Program si vyžádá od uživatele přihlašovací jméno a heslo a 
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
username = input("Username: ")
chosen_password = input("Password: ")

# pokud uživatel není registrovaný, upozorni jej a ukonči program.
if username not in users:
    print("Unregistered user, terminating the program.")

else:
    passwords = passwords[users.index(username)]

# pokud je uživatel registrovaný, ale zadá špatné heslo, sděl mu tuto informaci
    if passwords != chosen_password:
        print(f"You input wrong password, {username}")

# pokud je registrovaný a zadá správné heslo, pozdrav jej a umožni mu analyzovat texty       
    else:             
        print(
            separator,
            f"Welcome to the app, {username}",
            "We have 3 texts to be analyzed.",
            separator, sep="\n"
        )
        
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
           
# Pro vybraný text spočítá počet slov:
            words = list()

            for word in text.split():
                words.append(word.strip(",.;:"))
            
            titlecase = 0
            uppercase = 0
            lowercase = 0
            numeric = 0
            sum_of_numbers = 0
            
            for word in words:
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
               
            print(
                separator,
                f"There are {len(words)} words in the selected text.",
                f"There are {titlecase} titlecase words.",
                f"There are {uppercase} uppercase words.",
                f"There are {lowercase} lowercase words.",
                f"There are {numeric} numeric strings.",
                f"The sum of all the numbers {sum_of_numbers}", 
                separator, sep="\n"
            )
          
# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.                       
            word_length = dict()
            
            for word in words:
                if len(word) not in word_length:
                    word_length[len(word)] = 1
                else:
                    word_length[len(word)] += 1

            word_length_list = list(word_length.keys())
            word_length_list.sort()
            sorted = {i: word_length[i] for i in word_length_list}

            longest_word = max(word_length.values())

            print("LEN|", "OCCURENCES".center(longest_word), "|NR", sep="")
            print(separator)

            for key in sorted:
                print(
                    f"{key: >3}|{("*" * sorted[key]).ljust(
                        longest_word)}|{sorted[key]}"
                    )
               
                