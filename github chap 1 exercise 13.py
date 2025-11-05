def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

nums = [2, 3, 4, 5]
print("List:", nums)
print("Product of list items:", product_of_list(nums), "\n")
