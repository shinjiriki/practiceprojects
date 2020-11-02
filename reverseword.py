# Reverse Words
# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

def reverse_words(text):
    word = []
    for i in text.split():
        word.append(i[::-1])
    word = ' '.join(word)
    return word
    # return ' '.join(s[::-1] for s in text.split(' '))


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('apple'))
print(reverse_words('a b c d'))
print(reverse_words('double  spaced  words'))
print(reverse_words('stressed desserts'))
print(reverse_words('hello hello'))
