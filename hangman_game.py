# actual procedure
while True:
    print("Lets play!")
    while True: #this is to get the amount of attempts
        attempts = input("how many incorrect attempts do you want?: ")
        try:
            int(attempts)
        except ValueError:
            print("sorry "+attempts+" is an invalid input, please input integer between 1 and 20")
        if int(attempts) > 20 or int(attempts) < 1:
            print("sorry "+attempts+" is an invalid input, please input integer between 1 and 20")
        else:
            attempts = int(attempts)
            break    
    while True: #asking for the length of the word
        wordlen = input("how many characters long do you want the word to be?: ")
        try:
            int(wordlen)
        except ValueError:
            print("sorry "+wordlen+" is an invalid input, please input integer between 1 and 20")
        if wordlen(attempts) > 10 or wordlen(attempts) < 4:
            print("sorry "+wordlen+" is an invalid input, please input integer between 1 and 20")
        else:
            wordlen = int(wordlen)
            break

    #actual procedure of guessing starts here