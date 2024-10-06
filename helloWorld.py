print("helloWorld bbg")

daf = 5;

get = 6;

var = get + daf;

print(var)
#Guess the Word
#Created by Miracle McGlown

#Imports random.
import random

#List of words.
wordList = ['sickness', 'serve', 'nomination', 'loot', 'commission', 'dump', 'smooth']

#Chooses random word from list.
item = random. choice(wordList) # Chooses from list.
print(item) # Prints choice.

#initialized variable and lists
guessedLetters = []
usedLetters = []
stars = list(item)
word = ['_']*len(stars)
print(word)
print(stars)
letter = ''

#Prints hanging post.
print("\n+---+")
print("    |")
print("    |")
print("    |")
print("   ===")

#Defines findIndex function.
def findIndex(users_letter):

  #Sets i to 0.
  i = 0

  #creates empty list
  indexList = []

  #looks for index of users_letter
  while i < len(stars):
    try:
      #Creates local variable to store the users letter index.
      result = stars.index( users_letter, i, len(stars))
      indexList.append( result)

    #Breaks when there is a valuee error.
    except ValueError:
      break

    #Sets i to result plus 1.
    i = result+1

  #returns index list.
  return indexList

#Sets lives to 6.
#Variable
lives = 6

#Makes sure the code repeats six times.
for x in range(6):

  #Checks if users lives are greater than 0 to enter while loop.
  while lives  > 0:

    #Lets user enter a letter to guess the word.
    letter = input('enter ').lower()

    usedLetters.append(letter)
    print('Used Letters:' , usedLetters)
    #Checks if letter is not in stars list and subtracts lives by one
    if letter not in stars:
      lives-=1

    #Checks if letter is in stars list and changes the word index to letter guessed.
    if letter in stars:
      for indexList in findIndex(letter):
        word[indexList] = letter

    #These pring the hang post depending on how many lives the user has left.
    if(lives == 6):
      print("\n+---+")
      print("    |")
      print("    |")
      print("    |")
      print("   ===")
    elif(lives == 5): 
      print("\n+---+")
      print("O   |")
      print("    |")
      print("    |")
      print("   ===")
    elif(lives == 4):
      print("\n+---+")
      print("O   |")
      print("|   |")
      print("    |")
      print("   ===")
    elif(lives == 3):
      print("\n+---+")
      print(" O  |")
      print("/|  |")
      print("    |")
      print("   ===")
    elif(lives == 2):
      print("\n+---+")
      print(" O  |")
      print("/|\ |")
      print("    |")
      print("   ===")
    elif(lives == 1):
      print("\n+---+")
      print(" O  |")
      print("/|\ |")
      print("/   |")
      print("   ===")
    elif(lives == 0):
      print("\n+---+")
      print(" O   |")
      print("/|\  |")
      print("/ \  |")
      print("    ===")
    
    print('Word' , word)

    #Checks is word equals stars list and gives congradulations message.
    if word == stars:
      print('You win!')
      break

#prints game over message if user fails to guess letter.
else:
    print('game over')

