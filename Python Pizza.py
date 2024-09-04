print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want ? S,M,L ")
pep = input("Do you want pepperoni on your pizza ? Y or N ")
cheese = input("Do you want extra cheese ? Y or N ")
rate = 0
if size == "S" :
    rate = 15
elif size == "M":
    rate = 20
else:
    rate = 25
if pep == "Y":
    if size == "S":
        rate += 17
    if size == "M":
        rate += 23
    if size == "L":
        rate += 28
if cheese == "Y":
    rate += 1
print(f"Your final bill is ${rate}.")
