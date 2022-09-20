# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Решение 1
text = 'Связался тарабвкан с лучшим кроабвм-сгорабви умри как все'
words = text.split()
letters = 'абв'
new_words = []
for word in words:
    if letters not in word:
        new_words.append(word)
print (new_words)
# Решение 2
text = 'Связался тарабвкан с лучшим кроабвм-сгорабви умри как все'

def new_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = new_words(text)
print(text)