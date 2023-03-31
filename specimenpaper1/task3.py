# Question 3

word = input()
long_word = word

while len(long_word) <= 30:
    long_word = long_word + word
    
print(long_word)
