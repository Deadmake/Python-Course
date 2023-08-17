import os

while True:
    print("\033[96m" + """
        
    8888888b.  8888888b.   .d88888b.  888b     d888 8888888 888      888      8888888888 
    888   Y88b 888   Y88b d88P" "Y88b 8888b   d8888   888   888      888      888        
    888    888 888    888 888     888 88888b.d88888   888   888      888      888        
    888   d88P 888   d88P 888     888 888Y88888P888   888   888      888      8888888    
    8888888P"  8888888P"  888     888 888 Y888P 888   888   888      888      888        
    888        888 T88b   888     888 888  Y8P  888   888   888      888      888        
    888        888  T88b  Y88b. .d88P 888   "   888   888   888      888      888        
    888        888   T88b  "Y88888P"  888       888 8888888 88888888 88888888 8888888888 \033[92m
    \033[92m version:\033[1;30m 1.0.0 
    \033[92m Author: \033[1;30m Maggus 
    \033[0m                                                                                                                 
    """)

    AlkG = float(input("Wie viel Gramm Alkohol hast du getrunken? "))
    Weight = float(input("Wie viel wiegst du? "))
    Stunden = float(input("Wie viele Stunden sind seit dem letzten Drink vergangen? "))

    Promille = round(AlkG / (Weight * 0.7) - 0.15 * Stunden, 2)

    if AlkG <= 0 or Weight <= 0 or Stunden <= 0:
        print("\033[91m" + "404 - ERROR")
        input("Drück ENTER um fortzufahren...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif Promille < 0.5:
        print("Du darfst noch Auto Fahren, weil du nur " + "\033[92m" + str(Promille) + "\033[0m" + " Promille hast.")
        input("Drück ENTER um fortzufahren...")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Du darfst nicht mehr Auto Fahren, weil du " + "\033[92m" + str(Promille) + "\033[0m" + " Promille hast.")
        input("Drück ENTER um fortzufahren...")
        os.system('cls' if os.name == 'nt' else 'clear')