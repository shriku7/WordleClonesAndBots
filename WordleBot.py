def options(letters):
    Wordlist = open("wordlist.txt").read().split(",")
    lettersNew = [char for char in letters]
    b = []
    for x in Wordlist:
        k = 0
        for j in lettersNew:
            if j in x:
                k += 1
        if k == len(lettersNew):
            b.append(x)
    finallist = ''
            
    for x in b:
        if x == b[-1]:
            finallist += x
        else:
            finallist += x+', '

    return finallist
        

letters = str(input('Enter letters in word here: '))
result = options(letters)
print('The words you can use are: ' +  result)

