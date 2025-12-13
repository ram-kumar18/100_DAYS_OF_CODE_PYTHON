# TIP CALCULATOR

print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? %"))
total_people = int(input("How many people to split the bill? "))

final_bill = (total_bill + (total_bill * tip / 100)) / total_people # final_bill = total_bill + (total_bill * tip / 100) / total_people 
#                                                                     isme BODMAS ke vajah se bracket toh solve ho rha hai 
#                                                                     but then divide ho ja rha hai bina tip calculate kiye
print(f"Each person should pay: ₹{final_bill:.2f}")  # .2f is used to round off the number to 2 decimal places