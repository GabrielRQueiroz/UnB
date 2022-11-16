def palindrome(word):
    word = word.lower()
    inverse = word[::-1]

    if word != inverse:
        divergent_letters = 0
        for letter in word:
            if letter != inverse[word.index(letter)]:
                divergent_letters += 1

            if divergent_letters > 2:
                return "IMPOSSÍVEL"
    elif word == inverse:
        if len(word) % 2 == 0:
            return "IMPOSSÍVEL"

    return "POSSÍVEL"
