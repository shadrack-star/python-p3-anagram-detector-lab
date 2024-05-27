# your code goes here!
# lib/anagram.py
class Anagram:
    def __init__(self,word):
        self.word=word.lower()
    
    def is_anagram(self, other_word):
        return sorted(self.word) == sorted(other_word.lower())
    
    def match(self,word_list):
        return [word for word in word_list if self.is_anagram(word)]