import pygame
import random

pygame.init()
screen=pygame.display.set_mode((800,600))  # 创建屏幕
pygame.display.set_caption('飞机大战')  # 设置标题
icon=pygame.image.load('ufo.png')  # 导入图片图片
pygame.display.set_icon(icon)  # 添加进来
bgImg=pygame.image.load('bg.png')  # 添加背景
playerImg=pygame.image.load('player.png')  # 添加飞机
playerX=400
playerY=500
playerXStep=0  # 控制移动的
playerYStep=0

class Enemy():
    def __init__(self):
        self.img=pygame.image.load('enemy.png')
        self.x=random.randint(200,600)
        self.y=random.randint(50,250)
        self.step=random.randint(2,6)

enemys=[]
number_of_enemy=10
for i in range(number_of_enemy):
    enemys.append(Enemy())

def show_enemy():  # 显示敌人
    for e in enemys:
        e.x+=e.step
        if e.x>736 or e.x<0:
            e.step=-e.step
            e.y+=40
        screen.blit(e.img,(e.x,e.y))

class Bullet():
    def __init__(self):
        self.img=pygame.image.load('bullet.png')
        self.x=playerX+16
        self.y=playerY+10
        self.step=10
bullets=[]  # 现有的子弹
# 显示并移动子弹
def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.y-=b.step
        if b.y<0:
            bullets.remove(b)


def process_event():  # ，处理事件，简化代码，写成一个函数
    global running
    global playerXStep
    global playerYStep
    for event in pygame.event.get():  # 得到外面的事件
        if event.type==pygame.QUIT:
            running=False
        # 判断按下了键盘
        if event.type==pygame.KEYDOWN:  # 表示按下了键盘
            if event.key==pygame.K_RIGHT:  # 表示按下了右方向键
                playerXStep=5
            elif event.key==pygame.K_LEFT:  # 表示按下了左方向键
                playerXStep=-5
            elif event.key==pygame.K_UP:  # 表示按下了上方向键，因为左上是0,0
                playerYStep=-5
            elif event.key==pygame.K_DOWN:  # 表示按下了下方向键
                playerYStep=5
            elif event.key==pygame.K_SPACE:  # 按下了空格
                b=Bullet()
                bullets.append(b)
        if event.type == pygame.KEYUP:  # 表示松开了键盘
            playerXStep = 0
            playerYStep = 0

def move_player():
    global playerXStep
    global playerYStep
    global playerX
    global playerY
    playerX+=playerXStep  # 让飞机动起来
    playerY+=playerYStep
    if playerX>736:  #  防止飞机出界
        playerX=736
    if playerX<0:
        playerX=0
    screen.blit(playerImg,(playerX,playerY))  # 画上飞机


running=True
while running:
    screen.blit(bgImg,(0,0))   # 屏幕上画一个图片，坐标是(0,0)
    process_event()
    show_enemy()
    show_bullets()
    move_player()


    pygame.display.update()  # 更新一下屏幕，这句话要放在修改后的屏幕最后，与pygame无关的代码放在这句话下面也行