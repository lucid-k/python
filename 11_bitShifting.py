def main():
    perm = {"r":0b100,"w":0b010,"x":0b001}
    curPerm = 0
    owner=0
    group=0
    other=0
    while True:
        uInput=input("\nMAIN MENU\n\nSelect\n1.To check the current permissions\n2.Edit Owner permissions\n3.Edit group permissions\n4.Edit other permissions\n5.Exit\n").strip()
        match uInput:
            case "1":
                curPerm = (owner<<6)|(group<<3)|other
                step=6
                if curPerm == 0:
                    print("No permissions set\n")
                else:
                    while step >= 0:
                        for name,value in perm.items():
                            if curPerm&(value<<step):
                                print(name,end=" ")
                            else:
                                print("-",end=" ")
                        step -=3
            case "2":
                while True:
                    uInput1=input("enter:\n\"r\" to toggle read\n\"w\" to toggle write\n\"x\" to toggle execute\n\"exit\" to go back to main menu\n").strip().lower()
                    match uInput1:
                        case "r":
                            if owner&perm["r"]:
                                sInput=input("permission already set\nType \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput=="yes":
                                     owner&= ~perm["r"]
                            else:
                                owner|=perm["r"]
                                print("Read permission set\n")
                        case "w":
                            if owner&perm["w"]:
                                sInput1=input("permission already set\ntype\"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput1=="yes":
                                    owner&= ~perm["w"]
                            else:
                                owner|=perm["w"]
                                print("Write permission set\n")
                        case "x":
                            if owner&perm["x"]:
                                sInput2=input("permission already set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput2=="yes":
                                    owner&= ~perm["x"]
                            else:
                                owner|=perm["x"]
                                print("Execute permission set\n")
                        case "exit":
                            break
                        case _:
                            print("wrong input try again\n")
            case "3":
                while True:
                     uInput2=input("Enter\n\"r\" to toggle read\n\"w\" to toggle write\n\"x\" to toggle execute\n\"exit\" to go back to main menu\n").strip().lower()
                     match uInput2:
                         case "r":
                             if group&perm["r"]:
                                 sInput3=input("permission alredy set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                 if sInput3=="yes":
                                     group&= ~perm["r"]
                             else:
                                 group|=perm["r"]
                                 print("Read permission set\n")
                         case "w":
                             if group&perm["w"]:
                                 sInput4=input("permission is already set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                 if sInput4 == "yes":
                                     group&= ~perm["w"]
                             else:
                                 group|=perm["w"]
                                 print("Write permission set\n")
                         case "x":
                             if group&perm["x"]:
                                 sInput5=input("permission is already set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                 if sInput5== "yes":
                                     group&= ~perm["x"]
                             else:
                                 group|=perm["x"]
                                 print("Execute permission set\n")
                         case "exit":
                             break
                         case _:
                             print("wrong input try again\n")
            case "4":
                while True:
                    uInput3=input("Enter\n\"r\" to toggle read\n\"w\" to toggle write\n\"x\" to toggle execute\n\"exit\" to go to main menu\n").strip().lower()
                    match uInput3:
                        case "r":
                            if other&perm["r"]:
                                sInput6=input("Permission is already set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput6== "yes":
                                    other&= ~perm["r"]
                            else:
                                other|= perm["r"]
                                print("Read permission set\n")
                        case "w":
                            if other&perm["w"]:
                                sInput7=input("Permission set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput7=="yes":
                                    other&= ~perm["w"]
                            else:
                                other|=perm["w"]
                                print("Write permission set")
                        case "x":
                            if other&perm["x"]:
                                sInput8=input("Permission is set\ntype \"yes\" to toggle off\nanything else to continue\n").strip().lower()
                                if sInput8=="yes":
                                    other&= ~perm["x"]
                            else:
                                other|=perm["x"]
                                print("Execute permission set\n")
                        case "exit":
                            break
                        case _:
                            print("wrong input try again\n")
            case "5":
                print("sorry to see you leave\n")
                break
            case _:
                    print("Please enter the correct input\n")
main ()
