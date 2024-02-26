def count_bob_occurrences(text):
    count = 0
    pattern = ""

    for i in range(len(text)):

        if text[i] == 'b':
            if text[i:i + 3] == 'Bob':
                count += 1
    return count


# Example sentence
text = "Bob is a bobby boy who loves Bob."
print(count_bob_occurrences(text))

