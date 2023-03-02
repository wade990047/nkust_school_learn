# kg = float(input("體重:"))
# m = float(input("身高:"))
# bmi = kg/(m*m)
# print(bmi)

import requests

url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for i in range(1,51) :
  u = url.format(i)
  #r = requests.get(u)
  if i%2 == 0:
    print(u)

    