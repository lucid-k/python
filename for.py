import time

while True:
    print("Hello \nWhat would you like to do?\n1. Count down from a particular number\n2. see a series\n3. Count the multiples of a number within a range\n4. Exit\nNB: ONLY WORKS WITH POSITIVE INTEGERS\n")
    chs = input("What is your choice?\n")
    if chs.isdigit():
        num = int(chs)
        if num == 1:
            par = int(input("enter the number to count down from: "))
            j = par
            for i in range(par):
                print(f"{j}\n")
                j -= 1
                time.sleep(1) #waits for a second
            k = input("type exit to leave or anything else to try again ")
            if k.strip().lower() == "exit":
                break
            print("..................")
        elif num == 4:
            print("Thanks come again")
            break
        else:
            print("no such option try again\n**************")
    else:
        print("wrong input try again\n------------")


