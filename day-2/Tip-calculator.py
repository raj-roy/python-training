print("Welcome to the tip calculator.")
total_bill = round(float(input("What was the total bill? ")), 2)
tip_percentage = float(input("What percentage tip would you like to give? 10,  12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tips_amount = round(total_bill * tip_percentage / 100,  2)
total_amount = total_bill + tips_amount
each_person_pays = (total_amount / number_of_people)
each_person_pays = "{:.2f}".format(each_person_pays)
print(f"Each person should pay: {each_person_pays}")

