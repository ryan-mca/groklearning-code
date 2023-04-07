expenses = input("Enter the expenses: ").split()

amount = 0

for i in range(len(expenses)):
    amount+=int(expenses[i])

print(f"Total: ${amount}")