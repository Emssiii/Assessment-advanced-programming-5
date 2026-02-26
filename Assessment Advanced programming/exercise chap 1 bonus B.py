locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

print("Original list:", locations)
print("Length of list:", len(locations))
print("Alphabetical order:", sorted(locations))
print("Still original list:", locations)
print("Reverse alphabetical order:", sorted(locations, reverse=True))
print("Still original list:", locations)
locations.reverse()
print("After reverse():", locations)
locations.sort()
print("After sort():", locations)
locations.sort(reverse=True)
print("After reverse sort():", locations, "\n")
