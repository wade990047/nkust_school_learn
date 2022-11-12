# 21點作業框架程式
import random

#建立一個card_face串列，用來放所有牌面的花色，以下總共52個項目（每個花色各13個）
card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
#建立一個card_value串列，用來放所有牌面的點數，以下總共52個項目（每個花色各13個值，分別是1~13）
card_value = [i for i in range(1, 14)] * 4
#把前面兩個串列組合成一個串列deck，用來放所有的撲克牌內容（依照順序放），內容分別是('Diamond', 1), ('Diamond', 2), ..., ('Club', 13)
deck = [item for item in zip(card_face, card_value)]
#把deck串列中的牌順序打亂
random.shuffle(deck)
#建立一個用來存放所有玩家手上的牌的串列player_cards
num_players = int(input("請問這次要建立幾個玩家？"))
phand = []
pscores = []

for i in range(num_players):
    pcards = []
    for j in range(0,3):
        pcards.append(deck.pop())
    #在這邊為每個人發3張牌，然後放到player_cards中
    phand.append(pcards)
for i in range(num_players):
    score = 0
    for j in range(0,3):
        if phand[i][j][1] > 10:
            score = score + 10
        elif phand[i][j][1] == 1:
            if score+10 > 21:
                score = score + 1
            else:
                score = score + 10
        else:
            score = score + int(phand[i][j][1])
    if score > 21:
        print("Player #{}'s points is bust!".format(i+1))
        score = 0
    else:
        print("Player #{}'s points is".format(i+1),score)
    pscores.append(score)
    print(phand[i])
top = max(pscores)
if top != 0:
    print("================================================")
    print("Winner is {}, winner's points is {}".format(pscores.index(top)+1,top))
else:
    print("no one win this round!")