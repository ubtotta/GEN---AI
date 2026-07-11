import string
import emoji
import contractions
from textblob import TextBlob

class TEXT_NORMALIZATION:

    def __init__(self,data):
        self.data=data
        self.start()
    
    def start(self):
        print('''
            1) Converting to lower case
            2) Removing punctuations
            3) Removing Special Characters
            4) Handling emojis
            5) Removing Extra Spaces
            6) Contractions(Expanding the words and Abbrevations)
            7) Correcting the words
            ''')
        
    def strings_lower(self):
        self.data = self.data.lower()
    
    def removing_puntuations(self):
        chars=self.data
        pun=string.punctuation
        for char in pun:
            chars=chars.replace(char,'')
        self.data=chars

    def removing_spl_char(self):
        chars = self.data
        for char in chars:
            if not char.isalnum() and not ord(char)==32:
                chars=chars.replace(char,'')
        self.data=chars

    def handling_emoji(self,res):
        chars=self.data
        if res==1:
            emoji.replace_emoji(chars,'')
        else:
            emoji.demojice(chars)
    
    def removing_extra_spaces(self):
        chars=self.data
        self.data=' '.join(chars.split())
    
    def contractions_(self):
        chars=self.data
        self.data=contractions.fix(chars)
    
    def 
    
        
            
        
            


        
obj=TEXT_NORMALIZATION('corrting tHe wods& for txt,! normalization')
print(obj.removing_puntuations())
print(obj.removing_spl_char())
