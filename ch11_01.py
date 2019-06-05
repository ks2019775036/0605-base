import turtle as t                      #2019775036
                                        #양민철
draw_action = 1  
oldx = 0 
oldy = 0 
 
def new_clear(): 
    global draw_action
    global oldx
    global oldy
    t.clear()
    t.pensize(1)
    t.pendown()
    draw_action = 1
    oldx = 0
    oldy = 0
 
def draw(x,y):  
    global oldx
    global oldy
 
    if draw_action == 1:                #선 그리기 
        t.goto(x,y)
        oldx = x
        oldy = y
    elif draw_action == 2:              #삼각형 그리기
        t.goto(x, oldy)
        t.goto((x+oldx)//2, y)
        t.goto(oldx, oldy)
    elif draw_action == 3:              #사각형 그리기
        t.goto(x, oldy)
        t.goto(x,y)
        t.goto(oldx,oldy)
    elif draw_action == 4:              #원형 그리기
        t.circle(-((x-oldx)//2))        #클릭한 방향으로 원을 그림
 
def drag(x,y) :
    if draw_action== 1 :
        draw(x,y)
 
def move(x, y): 
    global oldx
    global oldy
    penstatus = t.isdown()              #현재 펜 업/다운 상태 저장
    t.penup()
    t.goto(x,y)
    if penstatus == True:
        t.pendown()
    oldx = x
    oldy = y
 
def key_l():
    global draw_action
    draw_action = 1
def key_t():
    global draw_action
    draw_action = 2
def key_r():
    global draw_action
    draw_action = 3
def key_c():
    global draw_action
    draw_action=4
def key_n():
    new_clear()
def key_u():
    t.penup()
def key_d():
    t.pendown()
def key_1():
    t.pensize(1)
def key_3():
    t.pensize(3)
def key_5():
    t.pensize(5)
 
t.setup(600,600)
s = t.Screen()
t.shapesize(2)
t.speed(0)
t.left(90)
new_clear()
 
t.ondrag(drag)
s.onkey(key_l,"l")                  #L키 => 선그리기
s.onkey(key_t,"t")                  #t키 => 삼각형 그리기
s.onkey(key_r,"r")                  #r키 => 사각형 그리기
s.onkey(key_c,"c")                  #c키 => 원형 그리기
s.onkey(key_n,"n")                  #n키 => 모두 지우기 
s.onkey(key_u,"u")                  #u키 => 펜 올리기
s.onkey(key_d,"d")                  #d키 => 펜 내리기
s.onkey(key_1,"1")                  #1키 => 선 두께 : 1
s.onkey(key_3,"3")                  #3키 => 선 두께 : 3
s.onkey(key_5,"5")                  #5키 => 선 두께 : 5
s.onscreenclick(draw,1)             #마우스 왼쪽 버튼 => 그리기
s.onscreenclick(move,3)             #마우스 오른쪽 버튼 => 좌표 이동하기
s.listen()
