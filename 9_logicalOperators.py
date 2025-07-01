import time

def main():
    while True:
        print("WELCOME")
        anim="*"
        for i in range(4):
            print(anim*(i+1))
            time.sleep(1)
        prompt1=input("Are you a new user?\nEnter yes to register\nAnything else to continue\n").strip().lower()
        user= ""
        password= ""
        if prompt1 == "yes":
            user=input("Enter your names:\n").strip
            password=input("Enter your password\n")
        
        break
main()

