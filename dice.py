import random
print("this is LUDO GAME")
x = "y"
while x == "y":
    DICE = random.randint(1,6)

    if DICE == 1:
        print("[______________]")
        print("[              ]")
        print("[              ]")
        print("[      O       ]")
        print("[              ]")
        print("[______________]")
    if DICE == 2:
        print("[______________]")
        print("[              ]")
        print("[              ]")
        print("[    O    O    ]")
        print("[              ]")
        print("[______________]")
    if DICE == 3:
        print("[______________]")
        print("[              ]")
        print("[      O       ]")
        print("[      O       ]")
        print("[      O       ]")
        print("[______________]")
    if DICE == 4:
        print("[______________]")
        print("[ O         O  ]")
        print("[              ]")
        print("[              ]")
        print("[ O         O  ]")
        print("[______________]")
    if DICE == 5:
        print("[______________]")
        print("[ O         O  ]")
        print("[              ]")
        print("[      O       ]")
        print("[ O         O  ]")
        print("[_____________]")
    if DICE == 6:
        print("[______________]")
        print("[              ]")
        print("[    O     O   ]")
        print("[    O     O   ]")
        print("[    O     O   ]")
        print("[______________]")
    x = input("press y to roll it again :")
