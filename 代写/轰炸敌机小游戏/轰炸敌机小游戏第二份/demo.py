import pygame
class Zidan1():
    def __init__(self):
        self.img=pygame.image.load('./bullet1.png')
        self.x=playerX+16
        self.y=playerY+16
        self.step=5
    def hit(self):
        global enemyY,enemyX,enemyXstep,enemyYstep,state,over
        if enemyX+50<self.x<enemyX+200 and enemyY+250<self.y<enemyY+260:
            enemyYstep+=0.2
            over+=1
        elif enemyX+200<self.x<enemyX+256 and enemyY+120<self.y<enemyY+130:
            enemyXstep-=0.1
            over+=1
        elif enemyX<self.x<enemyX+50 and enemyY+120<self.y<enemyY+130:
            enemyXstep += 0.1
            over+=1

class Zidan2():
    def __init__(self):
        self.img=pygame.image.load('bullet2.png')
        self.x=playerX+16
        self.y=playerY
        self.step=-5
    def hit(self):
        global enemyY,enemyX,state,over
        if enemyX+125<self.x<enemyX+135 and enemyY+135<self.y<enemyY+256:
            over=3
        elif enemyX+125<self.x<enemyX+135 and enemyY<self.y<enemyY+130:
            over=3



pygame.init()
screen=pygame.display.set_mode((800,400))  # 创建屏幕
pygame.display.set_caption('小飞机')  # 设置标题
bg=pygame.image.load('bg.png')  # 添加背景
playerImg=pygame.image.load('player.png')  # 添加飞机
playerX=400
playerXStep=0  # 控制左右移动的
playerY=0
playerYStep=0  # 控制上下移动的

enemyImg=pygame.image.load('enemy.png')  # 添加敌机
enemyY=300
enemyX=100
enemyYstep=-0.5
enemyXstep=0


zidan1=[]  # 现有的子弹
zidan2=[]
over=0
over_font=pygame.font.Font('C:/Windows/Fonts/msyh.ttc',64)


flag=True
while flag:
    screen.blit(bg,(0,0))   # 添加背景

    # 处理事件
    for event in pygame.event.get():  # 得到外面的事件
        if event.type==pygame.QUIT:
            flag=False

        if event.type==pygame.KEYDOWN:  # 表示按下了键盘
            if event.key==pygame.K_RIGHT:  # 表示按下了右方向键
                playerXStep=5
            elif event.key==pygame.K_LEFT:  # 表示按下了左方向键
                playerXStep=-5
            elif event.key==pygame.K_UP:  # 表示按下了上方向键
                playerYStep=-5
            elif event.key==pygame.K_DOWN:  # 表示按下了下方向键
                playerYStep=5
            elif event.key==pygame.K_SPACE:  # 按下了空格
                b=Zidan1()
                zidan1.append(b)
            elif event.key == pygame.K_a:  # 按下了A
                b=Zidan2()
                zidan2.append(b)
        if event.type == pygame.KEYUP:  # 表示松开了键盘
            playerXStep = 0
            playerYStep = 0

    # 展示敌人
    enemyX += enemyXstep
    enemyY += enemyYstep
    screen.blit(enemyImg, (enemyX, enemyY))

    # 展示子弹
    for b in zidan1:
        b.hit()  # 看看是否击中
        screen.blit(b.img, (b.x, b.y))
        b.y -= b.step
        if b.y < 0:
            zidan1.remove(b)
            break
    for b in zidan2:
        b.hit()  # 看看是否击中
        screen.blit(b.img, (b.x, b.y))
        b.x += b.step
        if b.y < 0:
            zidan2.remove(b)
            break

    # 移动飞机
    playerX += playerXStep  # 让飞机动起来
    playerY += playerYStep
    screen.blit(playerImg, (playerX, playerY))  # 画上飞机


    # 检查是否结束
    if over == 3:
        text = 'You Win!'
        score_rander = over_font.render(text, True, (255, 0, 0))  # 渲染一下字体，True表示使用24位色，元组表示三原色
        screen.blit(score_rander, (240, 180))
        enemyYstep = enemyXstep = 0

    pygame.display.update()  # 更新一下屏幕，这句话要放在修改后的屏幕最后，与pygame无关的代码放在这句话下面也行