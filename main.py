# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1 = "" ,word2 = ""):
    # [assignment] Add your code here
    
    word1 = input('Enter a word: ')
    word2 = input('Enter a word: ')
    
    word1.replace(' ',' ')
    word2.replace(' ',' ')
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    if sorted(word1) == sorted(word2):
        return True
    
    return False

print(find_anagram())

