print("Welcome to the tip calculator.")
bill_total = int(input("What was the total bill? "))
num_people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
multiplyer = 1 + (percentage/100)
bill_plus_tip = bill_total*multiplyer
personal_bill = round(bill_plus_tip/num_people,2)
print("Each person should pay: ${}".format(personal_bill))
print("Each persons tip is: ${}".format(round(personal_bill - bill_total/num_people, 2)))