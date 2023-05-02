from Turtle_new import Turtle_new
import turtle

def hajun(t3, str):
    # 얼굴
    t3.box(-150, -30, 120, 120, 'pink')
    # 눈 그리기
    t3.box(-125, 40, 20, 20, 'black')
    t3.box(-70, 40, 20, 20, 'black')

    # 메롱 입모양 만들기
    t3.merong(-123, 10)

    # 도발 글씨 쓰기.
    t3.print_provoke(-160, -80, 'blue', str)

    t3.hideturtle()

def hayul(t2, str):
    # 얼굴
    t2.box(30, -30, 140, 140, 'pink')
    # 눈
    t2.smile(50, 60, 40, 90, 'black')
    t2.smile(110, 60, 40, 90, 'black')
    # 입
    t2.smile(135, 10, 70, -90, 'black')
    # 볼터치
    #t2.box(50, 40, 15, 15, 'red')
    #t2.box(135, 40, 15, 15, 'red')
    t2.boltouch(50, 35, 10, 'red')
    t2.boltouch(130, 35, 10, 'red')

    # 도발 글씨 쓰기.
    t2.print_provoke(30, -80, 'blue', str)

    t2.hideturtle()

if __name__ == "__main__":
    turtle.setup(width=500, height=500)

    t3 = Turtle_new()
    t3.shape('turtle')
    hajun(t3, "조하준 메롱~")

    t2 = Turtle_new()
    t2.shape('turtle')
    hayul(t2, "조하율 공주")

    turtle.mainloop()