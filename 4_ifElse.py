gen = input("state your gender ").strip().lower()
#.strip() removes any additional spaces
#.lower() converts the string to lowercase
if gen in ["male","man","m"]:
    print(" Hello King")
else:
    print("Sorry you are not the target audience")

