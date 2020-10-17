f = open("text.txt", "r", encoding="UTF-8")
listText='['
for line in f:
    listText += '"' + line[:-1] + '",'
listText = listText[:-1]
listText += ']'
print(listText)