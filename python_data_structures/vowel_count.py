def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    frequency_map = {}

    for char in phrase.lower():
        in char in vowels:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    return frequency_map

print(vowel_count('rithm school'))
print((vowel_count('HOw ARE YOU? i am great!')))