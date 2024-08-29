import random

words = ["python", "javascript", "kotlin", "django", "ruby", "rust"]
word = random.choice(words)
word = word.upper()

total_chances = 7
guessesd_word = "-"*len(word)

while total_chances !=0:
      print("=============")
      print(guessesd_word)
      print("=============")
      letter = input("Guess a letter: ").upper()
      if letter in word: 
        for index in range(len(word)):
          if word [index]==letter:
            guessesd_word = guessesd_word[:index]+letter+guessesd_word[index+1:]
            #print(guessesd_word)
        if guessesd_word == word:
           print("================================")
           print("yaahoo! Congratulation you won!!") 
           print("================================") 
           break
      else:
         total_chances -= 1 
         print("Ohoo! Incorrect Guess")
         print("The remaining chances are: ", total_chances)
else:
    print("========================")
    print("GAME OVER")  
    print("========================") 
    print("You Lose :( ")
    print("========================")
    print("All the chances are exhausted")
    print("=============================")
print("The correct word is:" , word)





