#E-commerce management system

print("===== E-COMMERCE MANAGEMENT SYSTEM =====")

name = input("Enter customer name: ")

total = 0

# Products
products = {
    1: ["T-Shirt", 500],
    2: ["Jeans", 1200],
    3: ["Shoes", 2000],
    4: ["Watch", 1500],
    5: ["Bag", 800]
}

print("\n----- PRODUCTS -----")

for key,value in products.items():
    print(key, value[0], "Rs.", value[1])

# Taking Order

cart = []

for i in range(1, 4):

    choice = int(input("\nEnter product number (0 to stop): "))

    if choice == 0:
        break

    if choice in products:

        quantity = int(input("Enter quantity: "))

        product_name = products[choice][0]
        price = products[choice][1]

        amount = price * quantity
        total = total + amount

        cart.append([product_name, quantity, amount])

    else:
        print("Invalid product number!")


# Discount

if total > 5000:
    discount = total * 0.10
elif total > 2000:
    discount = total * 0.05
else:
    discount = 0


# Final Amount

final_amount = total - discount

print("\n===== ORDER BILL =====")
print("Customer Name:", name)

for product in cart:
    print(product[0], "x", product[1], "=", "Rs.", product[2])

print("----------------------")
print("Total Bill: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)

print("\nThank you for shopping with us!")