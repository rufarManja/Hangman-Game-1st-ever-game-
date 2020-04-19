# actual procedure
while True:
    print("Lets play!")
    while True: #this is to get the amount of attempts
        attempts = input("how many incorrect attempts do you want? [1-20]: ")
        try:
            if int(attempts) <= 20 and int(attempts) >= 1:
                attempts = int(attempts)
                break
        except ValueError:
            print("\n sorry "+attempts+" is an invalid input, please input integer between 1 and 20 \n")
        else:
            print("\n sorry "+attempts+" is an invalid input, please input integer between 1 and 20 \n")

    while True: #askin for the length of the word
        wordlen = input("how many characters long do you want the word to be?[4-10]: ")
        try:
            if int(wordlen) <= 10 and int(wordlen) >= 4:
                wordlen = int(wordlen)
                break
        except ValueError:
            print("\n sorry "+wordlen+" is an invalid input, please input integer between 4 and 10 \n")
        else:
            print("\n sorry "+str(wordlen)+" is an invalid input, please input integer between 4 and 10 \n") #str() in this one cos apprently it became an int before here
    x = 0 #for setting up cover
    cover = [] #will slowly be revealed 
    while x < wordlen: #sets up cover
        cover.append('*')
        x +=1
    print('cover',cover)
    cover = ''.join(cover)
    del x #dont need it afterwards
    wrongs = [] #this is for tracking all the wrong guesses

    word = get_word(wordlen) #!!NEED TO ADD THIS!!

    #actual procedure of guessing starts here
    while attempts > 0:
        print("word: "+cover)
        print("Previous guesses: "+wrongs)
        while True: #verifying the guess
            nxt = input(" \n input next guess")
            if wrongs.index(nxt) == True:
                print("already guessed this, try again")
            else:
                break
        if nxt in word:
            print("Good Guess!!")
            for i in word:
                word[i] = cover[i]
        else:
            print("incorrect guess")
            attempts -= 1
            wrongs.append(nxt) #adding the guess to the wrong guesses
        if '*' not in cover: #checking if solved
            print("CONGRATS YOU HAVE WON!!!")
            break
    #game is over now from here
    if attempts == 0:
        print("bad luck, can't win them all")
    again = input("Do you wanna play again?: ")
    if again == 'y' or again =='Y' or again == 'yes' or again == 'Yes':
        continue
    break
print("press enter to exit")
input() #hold the program open