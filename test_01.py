# write a function that takes a string argument and returns a number of vowels

def vowel_count(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in str.lower():
        if ch in vowels:
            count += 1

    return count 

# returns longest and shortest words from string 
def longest_and_shortest_words(str):
    words = str.split(" ")
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return [longest_word, shortest_word]

def test_with_my_first_name():
    assert vowel_count("Dima") == 2

def test_with_my_uppercase_name():
    assert vowel_count("DIMA SAFAROV") == 5

# print(vowel_count("Dima"))
# print(vowel_count("Safarov"))

print(longest_and_shortest_words("A cow is jumping on the tree")) 

def test_longest_and_shortest_words():
    assert longest_and_shortest_words("The cows coolest") == ["coolest", "The"]


     