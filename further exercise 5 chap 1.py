staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia",
         "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya",
         "Rafia", "Jake"]

count_dict = {}
for name in staff:
    count_dict[name] = count_dict.get(name, 0) + 1

print("Count of each staff member:")
for key, value in count_dict.items():
    print(f"{key}: {value}")
print()
