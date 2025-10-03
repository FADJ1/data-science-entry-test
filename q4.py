def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    reversed_string = ""
    
    # Simple loop going backwards through the string
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    
    return reversed_string


# Test the function
print("First test:", string_reverse("Hello World"))
print("Second test:", string_reverse("Python"))
