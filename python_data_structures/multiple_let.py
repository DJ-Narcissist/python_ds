def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count = {}
    for letter in string:
        letter_count[letter] = letter_count.get(letter,0) + 1
    return letter_count

result = multiple_letter_count("yay")
print(result)

cap_result = multiple_letter_count("Yay")
print(cap_result)