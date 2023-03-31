def cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if ord(char)%2 ==0:
                new_pos = (ord(char) - start + 5) %26
            else:
                new_pos = (ord(char) - start - 5) %26
            char = chr(start + new_pos)
        result += char
    return result
def main():
    phrase = "The quick brown fox jumps over the lazy dog"
    file_pointer_write = open("ch07/exercises/encrypted.txt", "w")
    file_pointer_write.write(cipher(phrase))
    file_pointer_write.close()

main()