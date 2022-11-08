word_dict = {}
word = input("Введите слова: ")
while word:
    if not word_dict.get(word):
        word_dict.update({word:word})
    word=input("Введите слова: ")
for word in word_dict.values():
    print(word)