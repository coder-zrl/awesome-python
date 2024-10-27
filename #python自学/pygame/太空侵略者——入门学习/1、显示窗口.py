import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))  # 创建屏幕
pygame.display.set_caption('飞机大战')  # 设置标题
icon=pygame.image.load('ufo.png')  # 导入图片图片
pygame.display.set_icon(icon)  # 添加进来
running=True
while running:
    for event in pygame.event.get():  # 得到外面的事件
        if event.type==pygame.QUIT:  # 如果点了XX
            running=False