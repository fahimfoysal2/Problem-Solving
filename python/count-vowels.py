# Count the number of each vowel in a given string.
#    Sample: "Hello, have you tried our tutorial section yet?"
#    Output: {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = {}
    for vowel in vowels:
        count[vowel] = string.count(vowel)
    return count

print(count_vowels("Hello, have you tried our tutorial section yet?"))
