from .exceptions import *
import random

class GuessAttempt(object):
    
    def __init__(self,character, hit=False, miss=False):
        self.character = character
        self.miss = miss
        self.hit = hit
        
        if hit and miss:
            raise InvalidGuessAttempt
            
        
    def is_hit(self):
        if self.hit:
            return True
        
        if not self.hit: 
            return False
                
        
    def is_miss(self):
        if self.miss: 
            return True
        
        if not self.miss: 
            return False
            

class GuessWord(object):
    def __init__(self, word_to_guess):
         
        self.answer = word_to_guess.lower()  
        
        if not word_to_guess:
            raise InvalidWordException
        else:
            self.masked = len(word_to_guess)*"*"
        

    def perform_attempt(self,character):
        character=character.lower()
        if not character or len(character) > 1:  
            raise InvalidGuessedLetterException


        if character not in self.answer:
            return GuessAttempt(character, hit= False, miss=True)
                
        
        if character in self.answer:
            masked_word = ''
            for index in range(0, len(self.answer)):
                if  character == self.answer[index]:
                    masked_word += character
                else:
                    masked_word += self.masked[index]

            self.masked = masked_word
            
            return GuessAttempt(character, hit= True, miss=False)
             
  


class HangmanGame(object):
    
    WORD_LIST = ['rmotr', 'python', 'awesome']
    
    def __init__(self, word_list=['rmotr', 'python', 'awesome'], number_of_guesses=5):
        self.word_list=word_list
        self.remaining_misses = number_of_guesses
        self.previous_guesses =[]
        # self.word= GuessWord(HangmanGame.select_random_word(self.word_list)) 
        self.word = GuessWord(self.select_random_word(word_list))
        
    
    
    def guess(self,character):
        character = character.lower()
        
        if self.is_finished():
            raise GameFinishedException
        
        self.previous_guesses.append(character)
        
        if self.word.perform_attempt(character).is_miss():
                self.remaining_misses -= 1
        
        if self.is_lost():
            raise GameLostException
        
        if self.is_won():
            raise GameWonException

            
        return self.word.perform_attempt(character)    




    def is_finished(self):
        if self.is_lost() or self.is_won():
            return True
        else: 
            return False
        
    def is_lost(self):
        if self.remaining_misses == 0:
            return True
        else: 
            return False
    
    def is_won(self):
        if self.word.answer == self.word.masked:
            return True
        else: 
            return False

    @classmethod 
    def select_random_word (cls,word_list):
        if not word_list:
            raise InvalidListOfWordsException
        else:
            return random.choice(word_list)
        
    
