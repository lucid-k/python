import time

while True:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nMAIN MENU:\nHello! \nWhat would you like to do?\n1. Count down from a particular number\n2. see a series\n3. Count the multiples of a number within a range\n4. Exit\nNB: ONLY WORKS WITH POSITIVE INTEGERS\n")
    chs = input("What is your choice?\n")
    if chs.isdigit():
        num = int(chs)
        if num == 1:
            while True:
                inp_a = input("enter the number to count down from: ")
                if inp_a.isdigit():
                    par=int(inp_a)
                    j = par
                    for i in range(par):
                        print(f"{j}\n")
                        j -= 1
                        time.sleep(1) #waits for a second
                    k = input("type 'exit' to go back to the main menu or anything else to try again\n ")
                    if k.strip().lower() == "exit":
                        break
                    print("...................................................")
                else:
                    print("Wrong input try again\n...................................................")
        elif num == 2:
            while True:
                inp = input("Enter the number to stop: ").strip()
                if inp.isdigit():
                    ends = int(inp)
                    ends += 1
                    inp2 = input("enter the number of steps to skip: ").strip()
                    if inp2.isdigit():
                        step=int(inp2)
                        for l in range (0,ends,step):
                            print(l,end=",")
                        print("\n")
                        leave = input("Enter 'exit' to go back to main menu or anything else to retry\n")
                        if leave.strip().lower()=="exit":
                            break
                        7
                    else:
                        print("wrong input try again \nooooooooooooooooooooooooooooooooooooooooooooooooooo")
                else:
                    print("incorrect input\nooooooooooooooooooooooooooooooooooooooooooooooooooo")
        elif num == 3:
            while True:
                inpA = input("Enter the number to start: ").strip()
                if inpA.isdigit():
                    strt = int(inpA)
                    inpB = input("enter the number to stop: ").strip()
                    if inpB.isdigit():
                        end=int(inpB)
                        end+=1
                        inpC = input("Enter the number to find multiples of: ")
                        if inpC.isdigit():
                            mult=int(inpC)
                            count=0
                            for m in range(strt,end):
                                if (m % mult)== 0:
                                    print(m,sep=",")
                                    count += 1
                            print(f"There are {count} multiples")
                            leave_b= input("Enter 'exit' to go back to the main menu or anything else to try again\n")
                            if leave_b.strip().lower() == "exit":
                                break
                            
                        else:
                            print("Enter a number\n###################################################")
                    else:
                        print("wrong input try again \nooooooooooooo")
                else:                                                  print("incorrect input\nooooooooooooooo")

        elif num == 4:
            print("Thanks come again")
            break
        else:
            print("no such option try again\n**************")
    else:
        print("wrong input try again\n---------------------------------------------------")


