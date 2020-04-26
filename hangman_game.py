#imports
import random
#functions
def get_word(wordlength:int):
    processed = 0 #amount words processed through
    current = str #current word being manipulated,will eventually be the one to be outputted by function
    W = open('Wordlist.txt',"r") 
    for word in W:
        if '(' in word or ')' in word:
            continue
        word = word.strip().lower() #makes sure the word is lower case and only contains characters and no spaces
        if len(word) < wordlength:#so wont spend time on words that are shorter than specfied
            continue
        processed += 1 #at this point the word has made it through conditions and now is going to try get picked
        if random.randint(1,processed) == 1: # as it goes on, becomes harder
            current = word
    return current




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
        wordlen = input("what is the minimum amount of characters you want the word to be?[4-10]: ")
        try:
            if int(wordlen) <= 10 and int(wordlen) >= 4:
                wordlen = int(wordlen)
                break
        except ValueError:
            print("\n sorry "+wordlen+" is an invalid input, please input integer between 4 and 10 \n")
        else:
            print("\n sorry "+str(wordlen)+" is an invalid input, please input integer between 4 and 10 \n") #str() in this one cos apprently it became an int before here
    word = get_word(wordlen)
    x = 0 #for setting up cover
    cover = [] #will slowly be revealed 
    while x < len(word): #sets up cover
        cover.append('*')
        x +=1
    del x #dont need it afterwards
    wrongs = [] #this is for tracking all the wrong guesses

    #!!NEED TO ADD THIS!!

    #actual procedure of guessing starts here
    while attempts > 0:
        print("word: "+ ''.join(cover)) #keeps cover as a list for later
        print("Previous guesses: "+str(wrongs))
        while True: #verifying the guess
            nxt = input(" \n input next guess: ")
            try:
                if nxt in wrongs:
                    print("already guessed this, try again")
                else:
                    break
            except ValueError: #means value isn't in list
                break

        if nxt in word:
            print("Good Guess!!")
            for i in range(len(word)):
                if word[i] == nxt:
                    cover[i] = nxt #this is where it is important cover is still a list, str doesnt support index assigning
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