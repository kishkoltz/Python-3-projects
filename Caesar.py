# D:\python3\app\python.exe Caesar.py
chars = [75, 114, 122, 121, 115, 122, 116, 111, 102]
for c in range(len(chars)):
    print (chr(chars[c]), end = '')
print ('')

text = input("Type in the message to be coded: ")
translated = ''
for symbol in text:
    num = ord(symbol)
    if num <100:
        num = str("0" + str(num))
    num = str(num)
    translated = translated+num

print (translated)
input()
n=3
word = [translated[i:i+n] for i in range (0, len(translated), n)]
print (word)
input()
for s in range(len(word)):
    print (chr(int(word[s])), end = '')
