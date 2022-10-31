data = []
f = open("bodyinfo.txt", "r", encoding="UTF-8")
dl = f.readlines() #讀取行數
f.close
name,h,w = dl[0].split(",")
name = name.strip()
h = h.strip()
w = w.strip()
for d in dl[1:]:
    sd = d.split(",")
    temp = dict()
    temp[name] = sd[0].strip()
    temp[h] = float(sd[1].strip())
    temp[w] = int(sd[2].strip())
    data.append(temp)
print(data)