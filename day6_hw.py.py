import turtle as t    
t.bgcolor("skyblue")  # 배경색을 하늘색으로 지정
t.speed(0)            # 거북이 속도를 가장 빠르게 지정
n = 30                # 동그라미를 그림 , 얼굴
t.color("white")     # 흰색으로 도형 내부 색칠
t.begin_fill()       # 색칠할 영역을 시작
for x in range(n):   # n번 반복
    t.forward(15)    # 15만큼 앞으로 이동
    t.left(360/n)    # 거북이가 360/n만큼 왼쪽으로 회전
t.end_fill()         # 색칠할 영역을 마무리 
t.left(190)          # 거북이가 190도 왼쪽으로 회전
n = 30               # 동그라미를 그림 , 몸통
t.color("white")     # 흰색으로 도형 내부 색칠
t.begin_fill()       # 색칠할 영역을 시작 
for x in range(n):   # n번 반복
    t.forward(22)    # 22만큼 앞으로 이동
    t.left(360/n)    # 거북이가 360/n만큼 왼쪽으로 회전
t.end_fill()         # 색칠할 영역을 마무리
t.up()               # 거북이 선을 숨김           
t.forward(20)        # 20만큼 앞으로 이동
t.right(100)         # 100도 오른쪽으로 회전
t.forward(90)        # 90만큼 앞으로 이동
t.down               # 움직이면 선이 그려짐
n = 15               # 동그라미를 그림 , 오른쪽 눈    
t.color("black")     # 펜의 색을 검정색으로 변경  
t.begin_fill()       # 색칠할 영역을 시작
for x in range(n):   # n번 반복
    t.forward(3)     # 3만큼 앞으로 이동
    t.left(360/n)    # 거북이가 360/n만큼 왼쪽으로 회전
t.end_fill()         # 색칠할 영역을 마무리 
t.up()               # 거북이 선을 숨김
t.right(95)          # 95도 오른쪽으로 회전
t.forward(60)        # 60만큼 앞으로 이동
t.down()             # 움직이면 선이 그려짐
n = 15               # 동그라미를 그림 , 왼쪽  눈
t.begin_fill()       # 색칠할 영역을 시작
for x in range(n):   # n번 반복
    t.forward(3)     # 3만큼 앞으로 이동
    t.left(360/n)    # 거북이가 360/n만큼 왼쪽으로 회전
t.end_fill()         # 색칠할 영역을 마무리
t.up()               # 거북이 선을 숨김
t.right(140)         # 140도 오른쪽으로 회전
t.forward(50)        # 50만큼 앞으로 이동
t.down()             # 움직이면 선이 그려짐     
t.color("orange")    # 펜의색을 주황색으로 변경
t.begin_fill()       # 색칠할 영역을 시작
t.left(150)          # 150도 왼쪽으로 회전
t.forward(40)        # 40만큼 앞으로 이동, 삼각형 밑변
t.left(150)          # 150도 왼쪽으로 회전
t.forward(45)        # 45만큼 앞으로 이동,  삼각형 윗변
t.left(110)          # 110도 왼쪽으로 회전
t.forward(23)        # 23만큼 앞으로 이동, 삼각형 높이
t.end_fill()         # 색칠할 영역을 마무리
t.up()              
t.right(25)
t.forward(23)        
t.down()
t.color("black")     # 펜의 색을 검정으로 변경
t.left(95)           # 입을 그리기 위한 각도 조절
t.pensize(3)         # 펜의 굵기 변경               
t.forward(30)
t.left(50)
t.forward(30)        # 입을 그림
t.up()
t.right(133)
t.forward(100)       
t.down()
t.pensize(1)         # 펜의 굵기 변경 
t.color("brown")     # 펜의 색을 갈색으로 변경
angle = 90           # 왼쪽으로 회전할 각도를 지정
for x in range(25):  # x 값을 0에서 24까지 바꾸면서 25번 실행
      t.forward(x)
      t.left(angle)  # 첫번째 단추
t.right(55)
t.up()
t.forward(55)        
t.down()               
angle = 90           # 왼쪽으로 회전할 각도를 지정
for x in range(25):  # x 값을 0에서 24까지 바꾸면서 25번 실행
       t.forward(x)
       t.left(angle) # 두번째 단추
t.right(160)
t.up()
t.forward(80)
t.down()
t.right(35)
t.begin_fill()       # 땅 색칠 시작
t.color("white")     # 펜의 색을 하얀색으로 변경 
t.forward(300)
t.left(90)
t.forward(100)
t.left(87)
t.forward(700)
t.left(91)
t.forward(100)
t.left(85)
t.forward(400)
t.end_fill()         # 땅 색칠 마무리
t.up() 
t.forward(100)
t.right(70)
t.forward(400)
t.down()                             
angle = 162
for x in range(35):
       t.forward(x)
       t.left(angle)  #첫번째눈
t.right(60)
t.up()
t.forward(155)
t.down() 
angle = 162
for x in range(35):
       t.forward(x)
       t.left(angle)   #두번째눈
t.right(180)
t.up()
t.forward(120)
t.down() 
angle = 162
for x in range(35):
       t.forward(x)
       t.left(angle)  #세번째눈
t.left(60)
t.up()
t.forward(200)
t.down()
angle = 162
for x in range(35):
       t.forward(x)
       t.left(angle)  #네번째눈
t.up()
t.left(20)
t.forward(200)
t.down()
angle = 162
for x in range(35):
       t.forward(x)   
       t.left(angle)   #다섯번째눈
t.up()
t.left(20)
t.forward(150)
t.down()
angle = 60
for x in range(20):
       t.forward(x)
       t.left(angle)
       t.circle(5)   #여섯번째눈
t.up()
t.right(40)
t.forward(150)
t.down()
angle = 60
for x in range(20):
       t.forward(x)
       t.left(angle)
       t.circle(5)   #일곱번째눈
t.up()
t.left(90)
t.forward(420)
t.down()
angle = 60
for x in range(20):
       t.forward(x)
       t.left(angle)
       t.circle(5)  #여덟번째눈
t.up()
t.right(46)
t.forward(165)
t.down()
angle = 50
for x in range(40):
       t.forward(x)
       t.left(angle)
       t.circle(6)    #아홉번째눈










       
























