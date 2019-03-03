dif = input("Enter temperature you want to convert (f/c):  ")

if (dif == "f"):
    c = input("Enter fahrenhiet you want to convert: ")
    c = int(c)
    result = (c * 9/5) + 32
    print(str(c) + " celsius is " +str(result)+ " in fahrenhiet")
elif(dif == "c"):
    f = input("Enter celsius you want to convert:")
    f = int(f)
    result = (f - 32) * 5/9
    print(str(f) + " fahrenhiet is " + str(result)+ " in celsius")
else:
    print("You had entered an invalid character")