##made by 2019100941권택준
import turtle as t
##터틀 모듈을 불러오며 as t 로 인하여 turtle함수를 t로 줄여서 사용가능하게 해줍니다.
import math
##math모듈을 불러옵니다.
##sin,cos,radians함수가 내장되어있습니다.

a_g = 9.8   #     "acceleration of gravity"    중력가속도
drawing_time = 0.1    #      시간간격 변수입니다. 값이 작아질수록 그래프의 그림이 더욱 촘촘해집니다.
ux = 0  #        x속도
uy = 0  #        y속도
dx = 0   #        x이동거리
dy = 0  #        y이동거리
velocity = 0 #  속도
angle = 0   #     각도

def draw_track (x,y):
    velocity = t.numinput("입력","속도 :",50,30,100)
    ##turtle.numinput():두개의 인자를 요청하는 함수이며, 첫 인자는 'prompt'두 번째 인자는'default'입니다.
    ##prompt는 입력하려고 하는 숫자를 설명하는 내용의 텍스트 'default'는 값을 입력하지 않았을 때 함수가 받아들일 값입니다.

    angle = math.radians(t.numinput("입력","각도",30,0,360))
    ## 도>라디안으로 바꿔주는 함수입니다. ex)radians(90)=1.57


    t. clearstamps() ## 화면의 모든 스탬프를 클리어합니다.
    t.hideturtle() ##거북이를 화면에서 숨기는 기능의 함수입니다. showturtle와 반대의 함수
    t.setpos(x,y) ## 좌표(x,y)로 이동 == t.goto(a,b)와 같은 함수
    t.showturtle() ##거북이를 화면에 표시하는 함수
    t.stamp()  ##현재위치에 스탬프 찍기

    hl = -(t.window_height() /2)
    #t.window_height() : 터틀창의 높이를 반환하는 함수

    ux = velocity * math.cos(angle)
    uy = velocity * math.sin(angle)

    while True:
        uy = uy + (-1*a_g)*drawing_time
        dy = t.ycor() + (uy*drawing_time) - (a_g*drawing_time**2) / 2
        ##t.ycor() : 현재위치의 y좌표 반환
        dx = t.xcor() + (ux*drawing_time)
        #t.xcor() : 현재위치의 x좌표 반환

        if dy > hl:
            t.goto(dx,dy)
            t.stamp()
        else:
            break ##완료시 반복문 탈출

t.setup(600,600)   #화면 창 크기 조절
t.shape("turtle") #거북이의 모양을 바꿔주는 함수 모양에는 'arrow','turtle','circle'등이 있습니다.
t.shapesize(0.5,0.5,0.5) #거북이의 폭과 길이의 스케일과 외곽선의 두께를 지정하는 함수
t.penup()   #펜 올리기
s=t.Screen()
s.onscreenclick(draw_track)
s.listen() ##키 입력모드 실행
t.mainloop() #==t.done() ##저의 개발환경이 '파이참'이라 터틀창이 바로 꺼지는 현상이 있었습니다. 이를 해결하기 위하여 쓴 함수입니다.##