VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    
    
    
    def __init__(self, name):
        self.name = name
        self.prizes = []
        self.prizeMoney = 0
        
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)
    
    
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def getMove(self, category, obscuredPhrases, guessed):
        print('{} has ${}\n'.format(self.name, self.prizeMoney))
        print('Category: {}'.format(category))
        print('Phrase: {}'.format(obscuredPhrases))
        print('Guessed: {}\n'.format(guessed))
        print("Guess a letter, phrase, or type 'exit' or 'pass':")
    

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficult):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficult
        
    def smartCoinFlip(self):
        if self.difficulty < random.randint(1, 10):
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        lst = [letter.upper() for letter in LETTERS if letter not in guessed]
        if self.prizeMoney < VOWEL_COST:
            lst = [letter for letter in lst if letter not in VOWELS]
        return lst
        
    def getMove(self,category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)        
        if len(lst) == 0:
            return 'pass'
        if self.smartCoinFlip():
            for letter in self.SORTED_FREQUENCIES:
                if letter in lst:
                    return letter
        else:
            return random.choice(lst)
         
        
        

