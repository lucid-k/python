nam = input("Enter your name ")
gen = input(f"{nam} Enter your gender pronouns ").strip().upper()
#.upper() method converts string into caps
if gen in ["HE","HIM"]:
    print(f"Hello King {nam}")
elif gen in ["SHE","HER"]:
    print(f"Hello Queen {nam}")
elif gen == "IT":
    print(f"Hello human {nam}")
else:
    print("Are you human ? :-) ")
