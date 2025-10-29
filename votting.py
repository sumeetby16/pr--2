age = int(input("Enter your age: "))

if age < 0:
    print("Age can't be negative")
elif age > 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
