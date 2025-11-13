a = int(input("Enter no:"))
b = int(input("Enter no:"))

c = a / b

f = open("myfile", "w")
f.write("Writing %d into file" % c)
f.close()

print("File closed")
