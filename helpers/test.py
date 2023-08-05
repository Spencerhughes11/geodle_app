guess = 'antigua and barbuda'
capitalized = []
if ' ' in guess:
    temp = guess.strip().split(' ')
    for word in temp:
        if word != 'and':
            word = word.capitalize()
        capitalized.append(word)

    guess = ' '.join(capitalized)
else:
    guess = guess.capitalize()

print(guess)