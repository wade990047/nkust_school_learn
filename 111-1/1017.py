'''
chi = int(input("chi="))
while chi>=0 or chi>100:
    eng = int(input("eng="))
    total = chi + eng
    avg = total/2
    print(total,avg)
    chi = int(input("chi="))
print("end")
'''
data = []
score = int(input("score="))
while score >= 0:
    data.append(score)
    score = int(input("score="))
print("最高分:",max(data))
print("最低分:",min(data))
print("總分:",sum(data))
print("平均:",round(sum(data)/len(data),2))