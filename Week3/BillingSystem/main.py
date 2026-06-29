from product import Product
from bill import Bill

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i+1}")
    name = input("Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    products.append(Product(name, price, quantity))

bill = Bill()

subtotal, tax, total = bill.calculate_bill(products)

print("\n----------- BILL -----------")
print(f"{'Product':15}{'Price':10}{'Qty':10}{'Total':10}")

for p in products:
    print(f"{p.name:15}{p.price:<10}{p.quantity:<10}{p.total_price():<10}")

print("-----------------------------")
print(f"Subtotal : ₹{subtotal:.2f}")
print(f"Tax (18%): ₹{tax:.2f}")
print(f"Final Bill: ₹{total:.2f}")