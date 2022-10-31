class Computer:
    logo = ''
    CPU = ''
    GPU = ''
    def playGame(self):
        print("玩游戏")
    def learn(self):
        print("学习")
    def watch(self):
        print("观影")
    def info(self):
        print(self.logo,self.GPU,self.CPU)
    #self = 对象本身，所以它不会作为函数的形参

#computer1 是Computer类的对象
# . : 的
computer1 = Computer()
computer1.logo = 'ROG'
computer1.GPU = 'RTX4090Ti'
computer1.CPU = 'Ryzen 7900'
computer1.playGame()
computer1.learn()
computer1.watch()
computer1.info()
