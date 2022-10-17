chi = int(input("chi="))
while chi>=0 or chi>100:
    eng = int(input("eng="))
    total = chi + eng
    avg = total/2
    print(total,avg)
    chi = int(input("chi="))
print("end")