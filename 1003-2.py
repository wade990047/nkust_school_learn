data = list()
total = 0
n = input("人數:")
for i in range(int(n)):
    score = int(input("輸入分數:"))
    data.append(score)
print("最高分:" , max(data))
print("最低分:" , min(data))
print("總平均:" , sum(data)/len(data))
print("總分" , sum(data))