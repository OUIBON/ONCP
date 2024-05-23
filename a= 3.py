letters = [0,1,2,3,4,5,6,7,8,9,10]
numbers = ["a","b","c","d","e","f","g","h","i","j","k"]

# Créer un mot et calculer son score
def word_score(word):
    score = 0
    for letter in word:
        if letter in numbers:
            score += letters[numbers.index(letter)]
    return score

# Convert letters to numbers
def convert_to_numbers(word):
    new_word = ""
    for letter in word:
        if letter.isdigit():
            index = int(letter)
            if index < len(numbers):
                new_word += numbers[index]
    return new_word

print(word_score("abc"))  # Output should be 3 (0+1+2)
print(convert_to_numbers("012"))  # Output should be "abc"
