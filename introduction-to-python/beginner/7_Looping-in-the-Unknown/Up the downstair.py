steps = int(input("How many steps? ")) + 1

print("__")

for i in range(2, steps):
  print(f"{'  ' * (i - 1)}|_")

print(f"{'__' * (steps - 1)}|")