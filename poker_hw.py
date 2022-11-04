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
  print("你的分數是:",b,"\n")
def setup():
  card_face = ["Diamond"]*13 + ["Spade"]*13 + ["Heart"] * 13 + ["Club"] * 13
  card_value = [i for i in range(1, 14)] * 4
  deck = [item for item in zip(card_face, card_value)]
  random.shuffle(deck)
  return deck

deck = setup()
player_cards = []
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
  if scoreout == 10.5:
    print("您贏了! 恭喜您剛好獲得10.5點")
    replay = input("是否再玩一次?(Y/N):").lower()
    if replay == "y":
      deck = setup()
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
  elif scoreout > 10.5:
    print("\n你的分數爆掉了")
    say(player_cards,scoreout)
    replay = input("是否再玩一次?(Y/N):").lower()
    if replay == "y":
      deck = setup()
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