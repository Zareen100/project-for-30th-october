def find_substrings(input_string):
    substrings = []
    n = len(input_string)
    
    # Iterate over all possible starting indices
    for i in range(n):
        # Iterate over all possible ending indices
        for j in range(i + 1, n + 1):
            substrings.append(input_string[i:j])
    
    return substrings

# Test the function
input_string = "abc"
print(find_substrings(input_string))
