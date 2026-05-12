''' replace the donkey word from donkey.txt file'''

word = "donkey"

with open("donkey.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"####")

with open("donkey.txt","w") as f:
    content = f.write(contentNew)
