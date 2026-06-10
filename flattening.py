# Function to flatten, classify and remove duplicates

def flatten_typed(nested): # Function to flatten a nested list and group values by type

    # Store values in separate buckets
    # we use set here so that it automatically handles duplicate values
    result = {
        "integers": set(),
        "floats": set(),
        "strings": set(),
        "booleans": set()
    }

    # Recursive function to traverse nested lists
    def helper(lst):

        for item in lst:

            # Goes deeper if the item is a list  
            if isinstance(item, list):
                helper(item)

            elif isinstance(item, bool):
                result["booleans"].add(item)

            elif isinstance(item, int):
                result["integers"].add(item)

            elif isinstance(item, float):
                result["floats"].add(item)

            elif isinstance(item, str):
                result["strings"].add(item)
           
            # Unsupported data types raise a TypeError as required by the problem statement.
            else:
                raise TypeError(f"Unsupported type: {type(item).__name__}")

    helper(nested)

    final_result = {}

    for key, value in result.items():
        if len(value) > 0:
            final_result[key] = sorted(list(value))

    return final_result


# Test 1
print(flatten_typed([1, [2, [3, 2]], 1, [4]]))

# Test 2
print(flatten_typed([3, ["apple", 1.5], ["apple", [2, 1.5, "banana"]]]))

# Test 3
print(flatten_typed([True, 1, False, [True, 0, [2, False]]]))

# Test 4
print(flatten_typed([1, [2, {"key": "val"}]]))
