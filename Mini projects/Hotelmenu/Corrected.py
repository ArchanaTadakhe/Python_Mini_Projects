# Define menu of restaurant
menu = {
    "Pizza": 600,
    "Pasta": 500,
    "Coffee": 200,
    "Water": 40,
    "Burger": 60,
    "Salad": 50
}

print("Welcome to Archana Resto and Cafe")
print("""
Pizza  : Rs.600
Pasta  : Rs.500
Coffee : Rs.200
Water  : Rs.40
Burger : Rs.60
Salad  : Rs.50
""")

# Create a variable to store total order amount
order_total = 0

# Take first order
item1 = input("Enter the name of the item you want to order: ")

if item1 in menu:
    order_total += menu[item1]
    print(f"{item1} added to your order.")
else:
    print(f"Sorry, {item1} is not available.")

# Display total bill
print(f"Total order payment: Rs.{order_total}")




# Restaurant Menu Program

menu = {
    "pizza": 600,
    "pasta": 500,
    "coffee": 200,
    "water": 40,
    "burger": 60,
    "salad": 50
}

print("=" * 50)
print("🍽️    WELCOME TO ARCHANA RESTO & CAFE    🍽️")
print("=" * 50)

print("\n📋 MENU CARD")
print("-" * 50)
print("🍕 Pizza   : Rs.600")
print("🍝 Pasta   : Rs.500")
print("☕ Coffee  : Rs.200")
print("💧 Water   : Rs.40")
print("🍔 Burger  : Rs.60")
print("🥗 Salad   : Rs.50")
print("-" * 50)

order_total = 0

item1 = input("\n👉 Enter item you want to order: ").lower()

if item1 in menu:
    order_total += menu[item1]
    print(f"✅ {item1.title()} added successfully!")
else:
    print(f"❌ Sorry! {item1.title()} is not available.")

choice = input("\nDo you want another item? (yes/no): ").lower()

if choice == "yes":
    item2 = input("👉 Enter second item: ").lower()

    if item2 in menu:
        order_total += menu[item2]
        print(f"✅ {item2.title()} added successfully!")
    else:
        print(f"❌ Sorry! {item2.title()} is not available.")

print("\n" + "=" * 50)
print("🧾 BILL SUMMARY")
print("=" * 50)
print(f"💰 Total Amount : Rs.{order_total}")
print("🙏 Thank You For Visiting!")
print("🌟 Visit Again 🌟")
print("=" * 50)