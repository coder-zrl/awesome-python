import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))  # 创建屏幕
pygame.display.set_caption('飞机大战')  # 设置标题
icon=pygame.image.load('ufo.png')  # 导入图片图片
pygame.display.set_icon(icon)  # 添加进来
bgImg=pygame.image.load('bg.png')  # 添加背景
playerImg=pygame.image.load('player.png')
playerX=400
playerY=500
playerStep=0  # 控制移动的

running=True
while running:
    screen.blit(bgImg,(0,0))   # 屏幕上画一个图片，坐标是(0,0)
    for event in pygame.event.get():  # 得到外面的事件
        if event.type==pygame.QUIT:
            running=False
        # 判断按下了键盘
        if event.type==pygame.KEYDOWN:  # 表示按下了键盘
            if event.key==pygame.K_RIGHT:  # 表示按下了右方向键
                playerStep=5
            if event.key==pygame.K_LEFT:  # 表示按下了左方向键
                playerStep=-5
        if event.type == pygame.KEYUP:  # 表示松开了键盘
            playerStep = 0

    screen.blit(playerImg,(playerX,playerY))  # 画上飞机
    playerX+=playerStep  # 让飞机动起来
    if playerX>736:  #  防止飞机出界
        playerX=736
    if playerX<0:
        playerX=0
    pygame.display.update()  # 更新一下屏幕，这句话要放在修改后的屏幕最后，与pygame无关的代码放在这句话下面也行