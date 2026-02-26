count = 0
choice = input("Do you want to continue? (Y/N): ").upper()
while choice == 'Y':
    count += 1
    choice = input("Do you want to continue? (Y/N): ").upper()
print("Loop executed", count, "times.\n")
