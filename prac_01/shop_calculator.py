number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    Price = float(input("Price of Item: "))
    total_price = total_price + Price
if total_price > 100.0:
    final_price = total_price * 0.9
    print(f"Total price for {number_of_items} is ${final_price: .2f}")
else:
    print(f"Total price for {number_of_items} is ${total_price: .2f}")

