print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large")
print("Type 'done' when finished ordering\n")

running_total=0.0

while True:
    size=input("Enter drink size: ").strip().lower()

    if size=="done":
        print()
        break
    
    if size=="small":
        price=3.50
        running_total+=price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${running_total:.2f}\n")
    elif size=="medium":
        price=4.50
        running_total+=price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${running_total:.2f}\n")
    elif size=="large":
        price=5.50
        running_total+=price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${running_total:.2f}\n")
    else:
        print("Invalid size! Please enter small, medium, large, or done.\n")

discount=0.0
if running_total>=20.00:
    discount=3.00

final_total=running_total-discount

print("=== Order Summary ===")
print(f"Subtotal: ${running_total:.2f}")
if discount>0:
    print(f"Loyalty discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}") 
print("Thank you for your order!")