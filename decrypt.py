import string
vowels = 'aeiou'
class Decrypt():
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
        for x in letters:
            dict[x] = letters[(letters.index(x) + shift)%26 ] 

        return dict
    
    def encrypt_message(self):
        msg = self.__message.split(" ")
        vowel_removed = []
        for word in msg:
            vowel_removed.append(self.remove_vowel(word))
        message = " ".join(vowel_removed)
        encrypted_message = ''
        for l in message:
            if l in self.build_shift_dictionary():
                encrypted_message += self.build_shift_dictionary()[l]
            else:
                encrypted_message += l
        return encrypted_message.upper()



            





x=Decrypt("MACHINE")
print(x.encrypt_message())
