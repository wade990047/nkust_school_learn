import random
player = [0]
com = [0]
while True:
  print("玩家的數字目前為:",sum(player))
  take = input("玩家是否繼續抽取(Y/N):").lower()
  if take == "y":
    card = random.randint(1,13)
    if card >= 11:
        card=0.5
    player.append(card)
    if sum(player) > 10.5:
        print("玩家的數字為:",sum(player),"你輸了!")
        print("莊家的分數是:",sum(com))
        break
  elif take == "n":
      card = random.randint(1,13)
      if card >= 11:
        card=0.5
      com.append(card)
      if sum(player) > sum(com):
          print("玩家贏了!")
          print("你的分數是:",sum(player))
          print("莊家的分數是:",sum(com))
          break
      elif sum(player) < sum(com):
          print("莊家贏了!")
          print("你的分數是:",sum(player))
          print("莊家的分數是:",sum(com))
          break
      else:
          print("雙方平手!")
          print("你的分數是:",sum(player))
          print("莊家的分數是:",sum(com))
          break