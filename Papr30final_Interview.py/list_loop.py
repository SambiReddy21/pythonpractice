words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    print(word)
    print(word,end="")
    print(len(word))
    
    
for word in range(len(words)):
    print(word)
    
i = 0
while i < len(words):
    print(words[i])
    i = i + 1
    
[print(x) for x in words]