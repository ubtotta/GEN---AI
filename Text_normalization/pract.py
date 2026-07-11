import string
import emoji
import contractions
from textblob import TextBlob

class TEXT_NORMALIZATION:

    def __init__(self,data):
        self.data=data
    
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
        print(f'Raw Text:\n{self.data}\n')
        self.string_lower()
        print('Converted to lower case successfully.\n')
        opt=int(input('Choose the options:\n1. Remove the punctuations and special characters\n2. Skip these two methods\n '))
        if opt==1:
            self.removing_puntuations()
            self.removing_spl_char()
            print('Removed the spaces and special characters successfully.\n')
        else:
            option=int(input('1. Replace the Emojis\n2. Demojice(conver to text)\n'))
            if option==1:
                self.handling_emoji(option)   
                print('Replaced emojis successfully.\n') 
            else:
                self.handling_emoji(option)
                print('Converted emojis to strings successfully.\n')
                
        self.removing_extra_spaces()
        print('Removed extra spaces successfully.\n')
        self.contractions_()
        print('Applied Contractions successfully.\n')
        self.correcting_words()
        print('Corrected the words successfully.\n')

        print(f'Normalized Text:\n{self.data}')

    def string_lower(self):
        chars=self.data.lower()
        self.data=chars
    
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
            self.data=emoji.replace_emoji(chars,'')    
        else:
            self.data=emoji.demojize(chars)

    def removing_extra_spaces(self):
        chars=self.data.split()
        j=' '.join(chars)
        self.data=j
    
    def contractions_(self):
        chars=self.data
        self.data=contractions.fix(chars)
    
    def correcting_words(self):
        chars=self.data
        self.data=TextBlob(chars).correct()

obj=TEXT_NORMALIZATION('CorRet the wods f@or    txt normalization!!😜😍💕.')
obj.start()

    
         
