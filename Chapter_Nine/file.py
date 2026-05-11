f = open("myfile.txt","r")
data = f.read()
if "Twinkle" in data:
    print("Twinkle present in myfile")
else:
    print("Twinkle  not present in myfile")
print(data)
f.close()
