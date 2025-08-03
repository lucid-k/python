def main():
    variable = {"IS_ALIVE" : 0b0001,"IS_INVINCIBLE" : 0b0010,"HAS_SHIELD" : 0b0100,"DOUBLE_DAMAGE" : 0b1000}

    status = variable["IS_ALIVE"] | variable["HAS_SHIELD"]
    while True:
        choice = input("Enter:\n1. Show status\n2. Add/Remove shield\n3. Toggle invisibility\n4. Toggle double damage\n5. Kill player\n6. Revive player\n7. exit\n").strip()
        if choice.isdigit() and choice in ["1","2","3","4","5","6","7"]:
            match choice:
                case "1":
                    for name, value in variable.items():
                        if status & value:
                            print(name)
                case "2":
                    if status & variable["HAS_SHIELD"]:
                        print("Shield is on!\n")

        else:
            print("Wrong choice try again!\n")
main()
