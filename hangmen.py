import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["love", "baboon", "camel", "awkward", "beekeepeer", "terrible", "keyhole",
             "wizard", "rickshaw", "puzzle", "peekaboo", "rhythm", "jukebox", "google", "microsoft"]
randwd = random.choice(word_list)
c = None
i = 0
while c != randwd:
    c = input("user choose the word : ")
    if c != randwd:
        i = i-1
        print("wrong try")
        print(stages[i])
        if i == -len(stages):
            print("you loose ")
            break
        else:
            pass
    else:
        print("you won")
        break
