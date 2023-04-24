class StringUtility:
    def __init__ (self, string):
        self.str = string #should never be overwritten

    def __str__ (self):
        return self.str
    
    def vowels(self):
        vowels = "aeiou"
        string = self.str
        vowel_counter = 0
        for ch in string:
            if vowels.__contains__(ch):
                vowel_counter += 1
            else:
                continue
        if vowel_counter >= 5:
            return 'many'
        else:
            return str(vowel_counter)
        
    def bothEnds(self):
        string = self.str
        if len(string) <= 2:
            return ''
        else:
            new_string = string[0]+string[1]+string[-2]+string[-1]
            return new_string
    
    def fixStart(self):
        string = self.str
        new_string = ''
        counter = 1
        if len(string) <= 1:
            return string
        else:
            first_char = string[0]
            for ch in string:
                if first_char.__contains__(ch) and not counter:
                    new_string += "*"
                else:
                    new_string += ch
                    if counter:
                        counter -= 1
            return new_string
        
    def asciiSum(self):
        string = self.str
        sum = 0
        for ch in string:
            sum += ord(ch)
        return sum
    
    def cipher(self):
        string = self.str
        length = len(string)
        new_string = ''
        for ch in string:
            start = ord('A') if ch.isupper() else ord('a')
            if ch.isalpha():
                new_string += chr(start+ ((ord(ch) - start + length) % 26))
            else:
                new_string += ch
        return new_string


