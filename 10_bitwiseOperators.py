def main():
    variable = {"IS_ALIVE" : 0b0001,"IS_INVINCIBLE" : 0b0010,"HAS_SHIELD" : 0b0100,"DOUBLE_DAMAGE" : 0b1000}

    status = variable["IS_ALIVE"] | variable["HAS_SHIELD"]
    while True:
        choice = input("Enter:\n1. Show status\n2. Add/Remove shield\n3. Toggle invisibility\n4. Toggle double damage\n5. Kill player\n6. Revive player\n7. exit\n").strip()
        if choice.isdigit() and choice in ["1","2","3","4","5","6","7"]:
            match choice:
                case "1":
                    if not(status & variable["IS_ALIVE"]):
                        print("PLAYER IS DEAD\n")
                    else:
                        for name, value in variable.items():
                            if status & value:
                                print(name)
                case "2":
                    if status & variable["HAS_SHIELD"]:
                        print("Shield is on!\n")
                        u_input=input("Do you want to switch off ?\ntype \"yes\" to switch off anything else to continue\n").strip().lower()
                        if u_input == "yes":
                           status ^= variable["HAS_SHIELD"]
                    else:
                        u_input0=input("Shield is off !\nType \"yes\" to turn on\n").strip().lower()
                        if u_input0 == "yes":
                            status |= variable["HAS_SHIELD"]
                case "3":
                    if status & variable["IS_INVINCIBLE"]:
                        print("Invincibility is on !\n")
                        u_input1 = input("Do you want to turn it off?\nType \"yes\" to toggle off anything else to continue\n").strip().lower()
                        if u_input1 == "yes":
                            status ^= variable["IS_INVINCIBLE"]
                    else:
                        u_input2=input("Invinsibility is off !\nType \"yes\"to turn it on anything else to continue\n").strip().lower()
                        if u_input2 == "yes":
                            status |= variable["IS_INVINCIBLE"]
                case "4":
                    if status & variable["DOUBLE_DAMAGE"]:
                        u_input3=input("Double damage is on !\nType \"yes\" to turn off or anything else to continue\n").strip().lower()
                        if u_input3 == "yes":
                            status ^= variable["DOUBLE_DAMAGE"]
                    else:
                        u_input4 = input("Double damage is off !\nType \"yes\" to turn on anything else to continue\n").strip().lower()
                        if u_input4 == "yes":
                            status |= variable["DOUBLE_DAMAGE"]
                case "5":
                    if status & variable["IS_ALIVE"]:
                        u_input5 = input("Player is alive !\nType \"yes\" to kill the player anything else and they survive\n").strip().lower()
                        if u_input5 == "yes":
                            status &= ~status
                    else:
                        print("player is already dead\n")
                case "6":
                    if status & variable["IS_ALIVE"]:
                        print("The player is already alive\n")
                    else:
                        status |= variable["IS_ALIVE"]
                case _:
                    print("It is sad to see you leave\n"+"_"*50)
                    break

        else:
            print("Wrong choice try again!\n")
main()
