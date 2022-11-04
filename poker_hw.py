import random

def scores(a,score):
  cards_half = 0.5
  if a >= 11:
      score = score + cards_half
  else:
      score = score + a
  return score
def say(a,b):
  print("\n你的手牌是:",a)
  print("你的分數是:",b)


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

scoreout = 0
i = 0
num = player_cards[i][1]
scoreout = scores(num,scoreout)
say(player_cards,scoreout)
answer = input("請問你要補牌嗎?(Y/N):").lower()
replay = "y"

while answer != "n" and replay != "n":
  player_cards.append(deck.pop())
  i = i + 1
  num = player_cards[i][1]
  scoreout = scores(num,scoreout)
  if scoreout > 10.5:
    print("\n你的分數爆掉了")
    say(player_cards,scoreout)
    print()
    replay = input("是否再玩一次?(Y/N):").lower()
    if replay == "y":
      card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
      card_value = [i for i in range(1, 14)] * 4
      deck = [item for item in zip(card_face, card_value)]
      random.shuffle(deck)
      player_cards = []

      scoreout = 0
      i = 0
      player_cards.append(deck.pop())
      num = player_cards[i][1]
      scoreout = scores(num,scoreout)
      say(player_cards,scoreout)
      answer = input("請問你要補牌嗎?(Y/N):").lower()
    else:
      break
  else:
    say(player_cards,scoreout)
    answer = input("請問你要補牌嗎?(Y/N):").lower()
    if answer == "n":
      say(player_cards,scoreout)
      break
say(player_cards,scoreout)