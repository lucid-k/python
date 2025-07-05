import time

def main():
    while True:
        print("WELCOME")
        anim="*"
        for i in range(4):
            print(anim*(i+1))
            time.sleep(1)
        user = "Anthony"
        password = "1234"
        while True:
            prompt1=input("Are you a new user?\nEnter yes to register\nAnything else to continue\n").strip().lower()
            if prompt1 == "yes":
                user=input("Enter your names:\n")
                password=input("Enter your password\n")
                if not user or not password :
                    print("-"*50)
                    continue
                elif user == " " or password == " ":
                    print("Name or password cannot be blank\n"+("-"*50))
                    continue
                else:
                    break
            else:
                prompt_validate=input(f"{user} please enter your password\n")
                if password == prompt_validate:
                    print("Welcome Back\n")
                    break
                else:
                    print("Wrong password!\n")
                    continue

        while True:
            role=input("Enter:\n1.Administrator\n2.User\n").strip()
            if not role.isdigit() or int(role) not in [1, 2]:
                print("Enter 1 or 2")
                continue
            access=input("Do you have access ?\nyes/no \n").strip().lower()
            if access not in ["yes","no"]:
                print("Choose yes or no")
                continue
            if int(role) == 1 and access == "yes":
                print(f"Welcome Administrator {user}")
                break
            elif int(role) == 2 and access == "yes":
                print(f"Welcome User {user}")
                break
            else:
                print("Sorry you do not have access!!\n")
                return #exits the main function
        prompt_exit=input("Would you like to exit the program(yes) or try again(type anything else) ?\n").strip().lower()
        if prompt_exit == "yes":
            print("sorry to see you leave\n"+("-"*50))
            break
main()

