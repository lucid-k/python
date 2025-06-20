nam = input("Enter your name ")
gen = input(f"{nam} Please enter your gender ").strip().lower()
if gen in ["male","man","m","female","woman","f"]:
    if gen in ["male","man","m"]:
        print("Hello King {}".format(nam))
    else:
        print("Hello Queen {}".format(nam))
else:
    print("You are not the target audience") 
