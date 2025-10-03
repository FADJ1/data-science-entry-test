def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key is already in the dictionary
    if key in dct:
        print("The key was already there with value:", dct[key])
        dct[key] = value  # update the value
    else:
        dct[key] = value  # add new key-value pair
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

print("--- First test ---")
result1 = update_dictionary({}, "name", "Alice")
print("Dictionary after update:", result1)

print("\n--- Second test ---") 
result2 = update_dictionary({"age": 25}, "age", 26)
print("Dictionary after update:", result2)
