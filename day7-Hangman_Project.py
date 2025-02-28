import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
tries = 6
word_list = ['abruptly', 'absurd',
             'abyss',
             'affix',
             'askew',
             'avenue',
             'awkward',
             'axiom',
             'azure',
             'bagpipes',
             'bandwagon',
             'banjo',
             'bayou',
             'beekeeper',
             'bikini',
             'blitz',
             'blizzard',
             'boggle',
             'bookworm',
             'boxcar',
             'boxful',
             'buckaroo',
             'buffalo',
             'buffoon',
             'buxom',
             'buzzard',
             'buzzing',
             'buzzwords',
             'caliph',
             'cobweb',
             'cockiness',
             'croquet',
             'crypt',
             'curacao',
             'cycle',
             'daiquiri',
             'dirndl',
             'disavow',
             'dizzying',
             'duplex',
             'dwarves',
             'embezzle',
             'equip',
             'espionage',
             'euouae',
             'exodus',
             'faking',
             'fishhook',
             'fixable',
             'fjord',
             'flapjack',
             'flopping',
             'fluffiness',
             'flyby',
             'foxglove',
             'frazzled',
             'frizzled',
             'fuchsia',
             'funny',
             'gabby',
             'galaxy',
             'galvanize',
             'gazebo',
             'giaour',
             'gizmo',
             'glowworm',
             'glyph',
             'gnarly',
             'gnostic',
             'gossip',
             'grogginess',
             'haiku',
             'haphazard',
             'hyphen',
             'iatrogenic',
             'icebox',
             'injury',
             'ivory',
             'ivy',
             'jackpot',
             'jaundice',
             'jawbreaker',
             'jaywalk',
             'jazziest',
             'jazzy',
             'jelly',
             'jigsaw',
             'jinx',
             'jiujitsu',
             'jockey',
             'jogging',
             'joking',
             'jovial',
             'joyful',
             'juicy',
             'jukebox',
             'jumbo',
             'kayak',
             'kazoo',
             'keyhole',
             'khaki',
             'kilobyte',
             'kiosk',
             'kitsch',
             'kiwifruit',
             'klutz',
             'knapsack',
             'larynx',
             'lengths',
             'lucky',
             'luxury',
             'lymph',
             'marquis',
             'matrix',
             'megahertz',
             'microwave',
             'mnemonic',
             'mystify',
             'naphtha',
             'nightclub',
             'nowadays',
             'numbskull',
             'nymph',
             'onyx',
             'ovary',
             'oxidize',
             'oxygen',
             'pajama',
             'peekaboo',
             'phlegm',
             'pixel',
             'pizazz',
             'pneumonia',
             'polka',
             'pshaw',
             'psyche',
             'puppy',
             'puzzling',
             'quartz',
             'queue',
             'quips',
             'quixotic',
             'quiz',
             'quizzes',
             'quorum',
             'razzmatazz',
             'rhubarb',
             'rhythm',
             'rickshaw',
             'schnapps',
             'scratch',
             'shiv',
             'snazzy',
             'sphinx',
             'spritz',
             'squawk',
             'staff',
             'strength',
             'strengths',
             'stretch',
             'stronghold',
             'stymied',
             'subway',
             'swivel',
             'syndrome',
             'thriftless',
             'thumbscrew',
             'topaz',
             'transcript',
             'transgress',
             'transplant',
             'triphthong',
             'twelfth',
             'twelfths',
             'unknown',
             'unworthy',
             'unzip',
             'uptown',
             'vaporize',
             'vixen',
             'vodka',
             'voodoo',
             'vortex',
             'voyeurism',
             'walkway',
             'waltz',
             'wave',
             'wavy',
             'waxy',
             'wellspring',
             'wheezy',
             'whiskey',
             'whizzing',
             'whomever',
             'wimpy',
             'witchcraft',
             'wizard',
             'woozy',
             'wristwatch',
             'wyvern',
             'xylophone',
             'yachtsman',
             'yippee',
             'yoked',
             'youthful',
             'yummy',
             'zephyr',
             'zigzag',
             'zigzagging',
             'zilch',
             'zipper',
             'zodiac',
             'zombie',
             ]
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
k = 0
a = random.randint(0, 213)
word = word_list[a]
chosen = []
guess = [""]
print("The answer is " + word)
for i in range(0, len(word)):
    chosen.append("_")
while True:
    char = input("Guess a letter: ")
    for i in guess:
        if char == i:
            k = 1
    if k == 1:
        print(f"You have already guessed {char}")
        k = 0
    else:
        guess.append(char)
    a = word.find(char)
    if a == -1:
        tries -= 1
    for i in range(0, len(word)):
        if char == word[i]:
            chosen[i] = char
    print(chosen)
    print(stages[tries])
    if tries == 0:
        break
    if word == "".join(chosen):
        break
if tries == 0:
    print("You Lose")
    print(f"The word was {word}")
else:
    print("You Win")
