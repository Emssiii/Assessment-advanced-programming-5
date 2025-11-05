int_list = [12, 45, 23, 67, 89, 34, 22, 9, 100, 56]
print("List elements:")
for val in int_list:
    print(val, end=" ")
print("\nHighest:", max(int_list))
print("Lowest:", min(int_list))

int_list.sort()
print("Ascending order:", int_list)

int_list.sort(reverse=True)
print("Descending order:", int_list)

int_list.append(77)
int_list.append(88)
print("After appending two elements:", int_list, "\n")
