f = open("myfile.txt","r")
data = f.read()
print(data)
f.close()

st = "Everything is possible"
fwrite = open("myfile.txt", "w")
t = fwrite.write(st)
print(t)
fwrite.close()

ft = open("myfile.txt","r")
datat = ft.read()
print(datat)
ft.close()