def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return
if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
return -1
x, y = y, x
print("Swapped values:", x, y)


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
print(swap("Apple", 10))  # Expect -1
swap(9, 17)               # Expect: Swapped values: 17 9
