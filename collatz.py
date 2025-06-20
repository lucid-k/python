def main():
    while True:
        inp =input("Enter a non negative number greater than zero or type exit to cancel the program: ").strip()
        if inp.isdigit():
            c0 = int(inp)
            if c0 > 0:
                step = 0
                while c0 > 1:
                    if (c0 % 2) == 0:
                        c0 /= 2
                    else:
                        c0 = 3*c0 + 1
                    step += 1
                    print(c0)
                print(f"steps: {step}")
            else:
                print("Enter a number greater than zero")
                print("......................")
        else:
            if inp.lower() == "exit":
                break
            print("Wrong input try again")
            print("_______________________")
main()

