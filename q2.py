def find_and_replace(lst, find_val, replace_val):
    """
    Replaces all occurrences of find_val with replace_val in the given list.
    
    Args:
        lst: List to search and modify
        find_val: Value to find in the list
        replace_val: Value to replace found items with
    
    Returns:
        List with all find_val occurrences replaced by replace_val
    """
    # Input validation
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    
    # Create new list with replacements
    result = []
    for item in lst:
        if item == find_val:
            result.append(replace_val)
        else:
            result.append(item)
    
    return result


# Demonstration of function usage
if __name__ == "__main__":
    # Test Case 1: Numeric replacement
    numbers = [1, 2, 3, 4, 2, 2]
    result1 = find_and_replace(numbers, 2, 5)
    print(f"Test 1 - Input: {numbers}")
    print(f"         Output: {result1}")
    print(f"         Replaced all 2's with 5's\n")
    
    # Test Case 2: String replacement
    fruits = ["apple", "banana", "apple"]
    result2 = find_and_replace(fruits, "apple", "orange")
    print(f"Test 2 - Input: {fruits}")
    print(f"         Output: {result2}")
    print(f"         Replaced 'apple' with 'orange'\n")
    
    # Additional test case showing edge case
    mixed = [1, "apple", 2, "apple", 3]
    result3 = find_and_replace(mixed, "apple", "fruit")
    print(f"Test 3 - Input: {mixed}")
    print(f"         Output: {result3}")
    print(f"         Mixed data types handled correctly")
