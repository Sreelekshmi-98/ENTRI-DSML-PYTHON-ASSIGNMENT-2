number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {number}:")
for i in range(1, limit + 1):
    print(number * i)


