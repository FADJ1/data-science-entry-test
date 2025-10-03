def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Simple check using modulus operator
    if num % divisor == 0:
        return True
    else:
        return False


# Test the function
print("10 divisible by 2?", check_divisibility(10, 2))
print("7 divisible by 3?", check_divisibility(7, 3))
