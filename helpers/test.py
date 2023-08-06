guess = 'democratic republic of the congo'
capitalized = []
if ' ' in guess:
    temp = guess.strip().split(' ')
    for word in temp:
        if word != 'and' or word != 'of' or word != 'the':
            word = word.capitalize()
        capitalized.append(word)

    guess = ' '.join(capitalized)
else:
    guess = guess.capitalize()

print(guess)