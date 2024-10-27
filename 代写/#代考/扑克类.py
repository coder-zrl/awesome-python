class Poker():
    def __init__(self,paimian,huase):
        self.huase=huase
            #['方块','梅花','红桃','黑桃']
        self.paimian=paimian
            #['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    def disp(self):
        return self.huase+self.paimian
    def exchange(self,p2):
        self.huase,p2.huase=p2.huase,self.huase

    def pk(self,p2):
        huase=[self.huase,p2.huase]
        huase=[['方块','梅花','红桃','黑桃'].index(i) for i in huase]
        if huase[0]<huase[1]:
            return self.disp()+'<'+p2.disp()
        elif huase[0]>huase[1]:
            return self.disp() + '>' + p2.disp()
        else:
            paimian=[self.paimian,p2.paimian]
            paimian = [['2','3','4','5','6','7','8','9','10','J','Q','K','A'].index(i) for i in paimian]
            if paimian[0] > paimian[1]:
                return self.disp() + '>' + p2.disp()
            elif paimian[0] < paimian[1]:
                return self.disp() + '<' + p2.disp()
            else:
                return self.disp() + '=' + p2.disp()
if __name__ == '__main__':
    p1=Poker('8','方块')
    p2=Poker('Q','梅花')
    p1.exchange(p2)
    p1.disp()
    print(p1.pk(p2),end='')
    p2.disp()
