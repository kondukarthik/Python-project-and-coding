try:
    f = open("anand.txt","w")
    a = int (input("Enter no"))
    b = int (input("Enter no"))
    c = a / b
    print(c)
    f.write(f"the value is {c}")

except ZeroDivisionError:
    print("its a zerodivisionerror")
    print("Please don't enter 0 for value b")

finally:
    f.close()
    print("File closed")
 