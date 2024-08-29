print("Welcome to the tip calculator!")
bill = float(input("What was the total bill ? $"))
tip = float(input("How much tip would you like to give ? 10,12 or 15 ?"))
split = int(input("How many people to split the bill ?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
final_amount = total_bill / split
print(f"The amount to be paid is {final_amount}")
