print(" RENT CALCULATOR PROJECT")

print(" ***************************Give the below information tp get the rent per person *************************")

rent = int(input("Enter you flat rent = "))
food = int(input("Enter you amount of food = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in flat = "))


#we are multiplying electricity_spend and unit because we can not directly add in whole bill it will not calculate accurate

total_bill= electricity_spend * charge_per_unit

output = (food+rent+total_bill) // persons

print(" Each person will pay = ", output)


print(" *************************** THIS IS YOUR FINAL RENT PER PERSON DO GPAY *************************")





