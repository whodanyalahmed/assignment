print("Voltage calculator")
print("-----------------\n")

i = input("Enter current to proceed: ")
r = input("Enter resistance to proceed: ")
i = int(i)
r = int(r)

v= i * r
print("voltage = "+ str(v)+ "v")