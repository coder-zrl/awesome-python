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

running=True
while running:
    screen.blit(bgImg,(0,0))   # 屏幕上画一个图片，坐标是(0,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(playerImg,(playerX,playerY))  # 画上飞机
    playerX+=5  # 让飞机动起来
    if playerX>736:  #  防止飞机出界
        playerX=736
    if playerX<0:
        playerX=0
    pygame.display.update()  # 更新一下屏幕，这句话要放在修改后的屏幕最后，与pygame无关的代码放在这句话下面也行