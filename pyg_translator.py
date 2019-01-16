# variables
pyg = 'ay'
sentance = ""
play = "y"

# game loop
while play == "y":
    sentance = ""
    newSentance = []
    originalInput = input('Enter a word or sentance: ')                 

    # make sure that the list isn't empty
    if len(originalInput) > 0:
        sentance = originalInput.split()

        # translate each word into pig latin   
        for word in sentance:     
            first = word[0]
            new_word = word + first + pyg
            new_word = new_word[1:len(new_word)]
            newSentance.append(new_word)

        # print out the results
        if len(newSentance) > 1:
            print ("Your new sentance is: ", end="")
        else:
            print("Your new word is: ", end="")
        
        for word in newSentance:
            print(word, end=" ")

    else:
        print('It\'s empty, you idiot!')

    #ask the user if they want to play again
    print()
    play = input('Do you want to translate another word?y/n: ')
    print("Thanks for playing!")
 
