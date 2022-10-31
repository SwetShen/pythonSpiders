'''
【案例,模拟顾客结账功能----计算优惠后的实付金额】

满500可享受9折优惠
满1000可享受8折优惠
满2000可享受7折优惠
满3000可享受6折优惠

'''

money = float(input("请付钱:"))

def pay(money):
    if money >= 3000:
        return money * 0.6
    elif money >= 2000:
        return money * 0.7
    elif money >= 1000:
        return money * 0.8
    elif money > 500:
        return money * 0.9

payed = pay(money)
print('已支付:',money,',找零:',money - payed)