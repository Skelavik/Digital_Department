

with open("input.txt","r",encoding="UTF8") as file:
    line = file.read()
    words = line.split()

for word in words:
    for letter in word:
        if letter.isdigit() == True:
            if word in words:
                words.remove(word)
            continue
print(words)





