#Defibe menus of resturant

menu= {"Pizza":600, "Pasta":500, "Coffee":200,"Water":40,"Burger":60,"Salad":50}

print(menu)

print("***********Welcome to Archana Resto and Cafe*******************")
print(" Pizza: RS.600\n Pasta:Rs.500\n Coffee:RS.200\n Water:Rs.40\n Burger:Rs.60\n Salad:Rs.50")

#create a variable to add order

Order_total=0
print("***************************************************************")
item1=input("Enter the name of item you want to order : ")
if item1 in menu:
    Order_total += menu[item1]
    print(f"{item1}Your order added ")
else:
    print(f"Not available {item1}")
print(f"Total order payment: Rs.{Order_total}")

