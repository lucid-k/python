while True:
    nam = input("Enter your name or type \"exit\" to leave the program \n")
    if nam.strip().lower() == "exit":
        break
    gen = input(f"{nam} Enter your gender pronouns or type 'exit' to leave the program \n").strip().upper()
#.upper() method converts string into caps
    if gen.lower() == "exit":
        break
    if gen in ["HE","HIM"]:
        print(f"Hello King {nam}")
        break
    elif gen in ["SHE","HER"]:
        print(f"Hello Queen {nam}")
        break
    elif gen == "IT":
        print(f"Hello human {nam}")
        break
    else:
        hum = input("Are you human ? :-) ")
        if hum.strip().lower() in ["yes","y"]:
            print("try again! ")
            print("____________")
        else:
            print("go in peace!")
            break 
