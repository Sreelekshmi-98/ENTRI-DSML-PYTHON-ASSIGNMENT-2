age = int(input("Enter your age: "))

full_price = 6.00

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price:.2f}")
