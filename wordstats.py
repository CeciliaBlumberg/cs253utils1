def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg


def outliers(user_string):
    words = user_string.split()
    shortest = words[0]
    longest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    return shortest, longest