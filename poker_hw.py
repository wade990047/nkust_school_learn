import random

#建立一個card_face串列，用來放所有牌面的花色，以下總共52個項目（每個花色各13個）
card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13

#建立一個card_value串列，用來放所有牌面的點數，以下總共52個項目（每個花色各13個值，分別是1~13）
card_value = [i for i in range(1, 14)] * 4

#把前面兩個串列組合成一個串列deck，用來放所有的撲克牌內容（依照順序放），內容分別是('Diamond', 1), ('Diamond', 2), ..., ('Club', 13)
deck = [item for item in zip(card_face, card_value)]

#把deck串列中的牌順序打亂
random.shuffle(deck)

#建立一個用來存放玩家手上的牌的串列player_cards
player_cards = list()

#把deck串列中的最後1張牌pop出來，放到player_cards串列中
player_cards.append(deck.pop())
cards_half = 0.5
print("你的手牌是:", player_cards)
answer = input("請問你要補牌嗎?(Y/N):").lower()
replay = "y"
score = player_cards[0][1]
i = 1
while answer != "n" or replay != "n":
  player_cards.append(deck.pop())
  cards = len(player_cards)
  if player_cards[i][1] >= 11:
      print(player_cards[i][1])
      score = score + cards_half
      print(score)
  else:
      score = score + player_cards[i][1]
      print(score)
  i = i + 1
  if score >= 10.5:
    print("你的分數爆掉了")
    print("你的手牌是:",player_cards)
    print("你的分數是:",score)
    print()
    replay = input("是否再玩一次?(Y/N):").lower()
    if replay == "y":
      card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
      card_value = [i for i in range(1, 14)] * 4
      deck = [item for item in zip(card_face, card_value)]
      random.shuffle(deck)
      player_cards = []
      player_cards.append(deck.pop())
      print("你的手牌是:", player_cards)
      answer = input("請問你要補牌嗎?(Y/N):").lower()
      score = player_cards[0][1]
      i = 1
    else:
      break
  else:
    print("你的手牌是:",player_cards)
    answer = input("請問你要補牌嗎?(Y/N):").lower()
    if answer == "n":
      print("你的手牌是:",player_cards)
      print("你的分數是:",score)
      break
  #在這裡面寫把牌加到player_cards串列中的程式
  #同時也要判斷，如果在補完牌之後，玩家的分數爆了，就要立即中斷程式
  #以下要寫，當玩家決定不加牌或是牌分數爆掉之後，要印出玩家的分數，以及他得到的牌
  #並詢問玩家是否要再玩一次。