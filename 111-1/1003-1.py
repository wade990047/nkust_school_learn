scores = []
while True:
    score = input("輸入分數(輸入end退出):")
    if score == "end":
        print("資料內容:" + str(scores))
        print("資料長度:" + str(len(scores)))
        print("資料型態:" + str(type(scores)))
        break
    else:
        print("輸入成績為:" + score)
        scores.append(score)