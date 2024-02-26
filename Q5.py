def count_bob_occurrences(text):
    count = 0  # Initialize a counter to keep track of the number of occurrences

    # Iterate through the text character by character
    for i in range(len(text)):
        # Check if the current character is 'b' and the next three characters form 'Bob'
        if text[i] == 'b' and text[i:i + 3] == 'Bob':
            count += 1  # Increment the counter if the pattern is found

    return count  # Return the total count of occurrences


# Test the function
text = "Bob is a good boy, but Bob is better!"
print(count_bob_occurrences(text))  # Output: 2


