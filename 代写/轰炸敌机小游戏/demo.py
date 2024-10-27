import pygame

pygame.init()
screen=pygame.display.set_mode((800,400))  # 创建屏幕
pygame.display.set_caption('轰炸敌机')  # 设置标题
bgImg=pygame.image.load('bg.png')  # 添加背景
playerImg1=pygame.image.load('player1.png')  # 添加飞机
playerImg2=pygame.image.load('player2.png')  # 添加飞机
playerX=400
playerXStep=0  # 控制左右移动的
playerY=0
playerYStep=0  # 控制上下移动的


enemyImg=pygame.image.load('enemy.png')  # 添加敌机
enemyY=300
enemyX=100
enemyYstep=-0.5
enemyXstep=0


def show_enemy():  # 显示敌人
    global enemyImg,enemyY,enemyX,enemyXstep,enemyYstep
    enemyX += enemyXstep
    enemyY+=enemyYstep
    screen.blit(enemyImg,(enemyX,enemyY))

class Bullet1():
    def __init__(self):
        self.img=pygame.image.load('bullet1.png')
        self.x=playerX+16
        self.y=350
        self.step=10
    def hit(self):
        global enemyY,enemyX,enemyXstep,enemyYstep,state,is_over
        if enemyX+50<self.x<enemyX+200 and enemyY+250<self.y<enemyY+260:
            state='击中机尾'
            enemyYstep+=0.2
            is_over+=1
        elif enemyX+200<self.x<enemyX+256 and enemyY+120<self.y<enemyY+130:
            state = '击中右翼'
            enemyXstep-=0.1
            is_over+=1
        elif enemyX<self.x<enemyX+50 and enemyY+120<self.y<enemyY+130:
            state = '击中左翼'
            enemyXstep += 0.1
            is_over+=1


class Bullet2():
    def __init__(self):
        self.img=pygame.image.load('bullet2.png')
        self.x=16
        self.y=playerY
        self.step=10
    def hit(self):
        global enemyY,enemyX,state,is_over
        if enemyX+125<self.x<enemyX+135 and enemyY+135<self.y<enemyY+256:
            state = '击中机身'
            is_over=3
        elif enemyX+125<self.x<enemyX+135 and enemyY<self.y<enemyY+130:
            state = '击中机头'
            is_over=3




bullets1=[]  # 现有的子弹
bullets2=[]
# 显示并移动子弹
def show_bullets():
    for b in bullets1:
        b.hit()  # 看看是否击中
        screen.blit(b.img,(b.x,b.y))
        b.y-=b.step
        if b.y<0:
            bullets1.remove(b)
            break
    for b in bullets2:
        b.hit()  # 看看是否击中
        screen.blit(b.img,(b.x,b.y))
        b.x+=b.step
        if b.y<0:
            bullets2.remove(b)
            break

# 攻击状态
state=0
font=pygame.font.Font('C:/Windows/Fonts/msyh.ttc',28)  # 微软雅黑
def shou_score():
    text=f'状态:{state}'
    score_rander=font.render(text,True,(67,205,128))  # 渲染一下字体，True表示使用24位色，元组表示三原色
    screen.blit(score_rander,(500,20))

is_over=0
over_font=pygame.font.Font('C:/Windows/Fonts/msyh.ttc',64)
def check_is_over():
    global enemyYstep,enemyXstep
    if is_over==3:
        text = 'Game Over'
        score_rander = over_font.render(text, True, (255, 0, 0))  # 渲染一下字体，True表示使用24位色，元组表示三原色
        screen.blit(score_rander, (240, 180))
        enemyYstep=enemyXstep = 0
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
                b=Bullet1()
                bullets1.append(b)
            elif event.key == pygame.K_a:  # 按下了A
                b=Bullet2()
                bullets2.append(b)
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
    screen.blit(playerImg1,(playerX,340))  # 画上飞机
    screen.blit(playerImg2, (0, playerY))


running=True
while running:
    screen.blit(bgImg,(0,0))   # 屏幕上画一个图片，坐标是(0,0)
    process_event()
    show_enemy()
    show_bullets()
    shou_score()
    move_player()
    check_is_over()

    pygame.display.update()  # 更新一下屏幕，这句话要放在修改后的屏幕最后，与pygame无关的代码放在这句话下面也行