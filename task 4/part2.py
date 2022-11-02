word_dict = {}
word = input()
while word:
    if not word_dict.get(word):
        word_dict.update({word:word})
    word=input()
print(word_dict)
for i in word_dict.keys ():
    print (i,end = " ")