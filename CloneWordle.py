import random

def wordle(word, main):
    letters = [x for x in word]
    mainletter = [x for x in main]
    check = []
    for x in range(0,10):
        if letters[x] == mainletter[x]:
            check.append("✓")
        elif letters[x] in mainletter:
            check.append("O")
        else:
            check.append("X")
    return check



wordlist = open("words.txt").read().split(",")
l = []
for x in wordlist:
    if len(x) == 10:
        l.append(x)
main = random.choice(wordlist)
print("You have 11 guesses to guess the randomly picked word, if a letter is correct and in the right place it will have a check, if its correct but in the wrong place it will have an O, else, it will have a X. You have 5 guesses.")

for x in range(11):
    word = input('What is your guess: ')
    while word not in l:
        word = input ('Word does not exist. Guess again: ')
    y = wordle(word,main)
    print(y)
print('word was ' + main)


