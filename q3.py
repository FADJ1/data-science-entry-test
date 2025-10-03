def update_dictionary(dct, key, value):
    # Check if key exists
    if key in dct:
        # Print old value
        print(dct[key])
    # Update dictionary
    dct[key] = value
    # Return updated dictionary
    return dct

# Test 1: Add new key
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# Test 2: Update existing key
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
