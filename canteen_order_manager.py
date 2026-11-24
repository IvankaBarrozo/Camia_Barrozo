orders = []

for i in range(1,6):
    order = input(f"Enter order {i}: ")
    orders.append(order)



print(f"Original Order: {orders}")


additional_order = input("Enter additional order: ")
orders.append(additional_order)
print(f"Updated Order: {orders}")


priority_order = input("Enter priority order: ")
orders.insert(0, priority_order)
print(f"Updated Order: {orders}")


find_item = input("Search for an order: ")

if find_item in orders:
    count = orders.count(find_item)
    first_index = orders.index(find_item)
    print(f"Number of Occurrences: {count}")
    print(f"First Index: {first_index}")
else:
    print("Order not found.")


cancel_order = input("Enter cancel order: ")

if cancel_order in orders:
    orders.remove(cancel_order)
    print(f"Updated Order: {orders}")
else:
    print("Order not found.")


if orders:
    removed_item = orders.pop()
    print("Removed last order:", removed_item)
else:
    print("No orders left to remove.")

total = len(orders)

print("===== FINAL ORDER REPORT =====")
print(f"Orders: {orders}")
print(f"Total Remaining Orders: {total}")


