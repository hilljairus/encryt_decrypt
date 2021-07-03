import string
vowels = 'aeiou'
class Encrypt():
    def __init__(self,message):
        self.__message = message

    def remove_vowel(self,word):
        word = word.lower()
        
        removed = ''
        for i in range(len(word)):
            
            if word[i] in vowels and i>=1 and i<=len(word)-2: #vowels that occur mid word
                if word[i+1] in vowels and i+1<len(word)-1: # next letter is a vowel and occur mid letter
                    removed += word[i]
                else:
                    continue
            else:
                removed += word[i]
        return removed
                    
    def build_shift_dictionary(self,shift=4):
        letters = string.ascii_lowercase
        dict = {}
        #dictionary to map letters with shifted index greater that 25
        extra = {
            22: '[',
            23: '\\',
            24: ']',
            25: '%'

        }
        for x in range(len(letters)):
            if x<22:
                dict[letters[x]] = letters[(x + shift)] 
            else:
                dict[letters[x]] = extra[x]

        return dict
    
    def encrypt_message(self):
        msg = self.__message.split(" ") #Turn to list
        vowel_removed = []
        for word in msg:
            if "." in word:
                word = word.strip(".")
                vowel_removed.append(self.remove_vowel(word)+".")
            else:
                vowel_removed.append(self.remove_vowel(word))
        message = " ".join(vowel_removed)
        encrypted_message = ''
        for l in message:
            if l in self.build_shift_dictionary():
                encrypted_message += self.build_shift_dictionary()[l]
            else:
                if(l=='.'):
                    encrypted_message += '2'
                else:
                    encrypted_message += l
        return encrypted_message.upper()
x=Encrypt("A SUBSET OF MACHINE LEARNING IS CLOSELY RELATED TO COMPUTATIONAL STATISTICS WHICH FOCUSES ON MAKING PREDICTIONS USING COMPUTERS.")
print(x.encrypt_message())