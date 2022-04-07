import images, random, words                                        #importing the Hangman Images from pre existing file

word = random.choice(words.word_list)                                 #to select the random words from the list
word = word.upper()                                             #converting to Upper case
display = list(len(word)*'_')                                    #printing the dashes to identifiy the number of letters in the word
lives = 6                                                       #chances given to the user
gameWon = False

def check_letter(letter,word):                                  #defining the function to check the letter or word
    for i in range (0,len(word)):
        letter = word[i]                                        
        if guess == letter: 
            display[i] = guess
    if '_' not in display:                                       #if there are no blank spaces in the string 
        return True
    else:
        return False

def status():
    print(images.hangman[6-lives])                              #printing the images of HangMan
    print(' '.join([str(e) for e in display]))                   #done for avoiding the output like this ['_','_','_','_','_','_'] 
    print("You have",lives,"Lives")                     

print("-"*100)
print("Welcome to HANGMAN!")
print("It's a",len(word),"letter Word")

while gameWon == False and lives > 0:
    status()
    guess = input("Guess a Letter or an Entire Word: ")
    guess = guess.upper()                                       #Type conversion

    if guess == word:
        gameWon = True
        display = word

    if len(guess) == 1 and guess in word:
        gameWon = check_letter(guess,word)
    else:
        lives -= 1
    status()

if gameWon:
    print("Well done, You guessed it correctly!")
else:
    print("Sorry, You have Failed!, the word was: ",word)