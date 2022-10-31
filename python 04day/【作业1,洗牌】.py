import random
# 生成扑克牌 54张

logo = ['♥','♠','♦','♣']
number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
joker = ['jocker','JOCKER']

cards = []

for i in logo:
    for j  in number:
        cards.append(i + j)
cards.extend(joker)

# print(cards)

player1 = []
# 洗牌
# 先分17张
for i in range(17):
    # 随机数
    n = random.randint(0,len(cards) - 1)
    # 将牌分给玩家
    player1.append(cards[n])
    # 从牌库中去除这张牌
    del cards[n]

print(player1)

player2 = []
# 洗牌
# 先分17张
for i in range(17):
    # 随机数
    n = random.randint(0,len(cards) - 1)
    # 将牌分给玩家
    player2.append(cards[n])
    # 从牌库中去除这张牌
    del cards[n]

print(player2)

print(cards)
