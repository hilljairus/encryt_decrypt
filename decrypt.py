import string
import re
import difflib
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def load_words(file_name):
    print("Loading word list from file...")
    with open(file_name) as word_file:
        valid_words = set(word_file.read().split())
    print("  ", len(valid_words), "words loaded.")
    return list(valid_words)

def numb_of_consonants(word):
    summed = sum([z in consonants for z in word])
    return summed

class Decrypt():
    def __init__(self,message):
        self.__message = message
        self.valid_words = load_words("words.txt")

                    
    def build_transpose_dictionary(self,shift=4):
        letters = string.ascii_lowercase
        dict = {}
        #dictionary to map letters with shifted index greater that 25
        extra = {
            22: '[',
            23: '\\',
            24: ']',
            25: '%'

        }
        
        for x in range(4, len(letters)):
            
            dict[letters[x]] = letters[x-shift] 
        for y in extra:
            dict[extra[y]] = letters[y]

        return dict
    
    def reshift_message(self):
        
        decrypted_message = ''
        for l in self.__message.lower():
            if l in self.build_transpose_dictionary():
                decrypted_message += self.build_transpose_dictionary()[l]
            else:
                if(l=='2'):
                    decrypted_message += '.'
                else:
                    decrypted_message += l
        return decrypted_message

    def decrypt_message(self):
        message_list = self.reshift_message().split(" ")
        msg = ""
        for word in message_list:
            # n = len(word)-1
            # related_words = re.findall(rf"\b{word[0]}\S+{word[n]}\b",self.valid_words)
            guesses = difflib.get_close_matches(word,self.valid_words)
            guesses = [y for y in guesses if numb_of_consonants(word)==numb_of_consonants(y) ]
            if '.' in word:
                if len(guesses)>=1:
                    msg += " " + str(guesses[0]) + '.'
    
                else:
                   msg += " " + "???" + '.' #If guess not found
            else:
                if len(guesses)>=1:
                    msg += " " + str(guesses[0]) #Take first guess
                else:
                    msg += " " + "???"

        return msg.strip().upper()


x= Decrypt("E PRK XQI EKS MR E KP\] JV JV E[]222")

#"QGLRI PIVRRK MW XLI WXH] SJ GQTXV EPKVXLQW XLX MQTVZI EXQXGPP] XLVSKL I\TVMRGI ERH "
print(x.decrypt_message())




