import turtle as t
import random
import time

def find_card(x,y):
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x,y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx

def score_update(m):
    score_pen.clear()
    score_pen.write(f"{m}   {score}점/{attempt}번 시도", False, "center", ("", 15))

def result(m):
    t.goto(0,-60)
    t.write(m,False, "center",("",30,"bold"))
def play(x,y):
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score

    if attempt == 12:
        result("Game Over")
        
    else:
        click_num += 1
        card_idx = find_card(x,y)
        turtles[card_idx].shape(img_list[card_idx])

        if click_num == 1:
            first_pick = card_idx
        elif click_num == 2:
            second_pick = card_idx
            click_num = 0
            attempt += 1

            if img_list[first_pick] == img_list[second_pick]:
                score += 1
                score_update("정답")
                if score == 8:
                    result("성")
            else:
                score_update("오답")
                turtles[first_pick].shape(default_img)
                turtles[second_pick].shape(default_img)

t.bgcolor("pink")
t.setup(700,700)
t.up()
t.ht()
t.goto(0,280)
t.write("카드 매칭 게임",False, "center", ("",30,"bold"))

#점수 펜 객체 생성
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0,230)

#터틀 객체 생성
turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color("pink")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)

default_img = "images/default_img.gif"
t.addshape(default_img)

img_list = []
for i in range(8):
    img = f"images/img{i}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)
    

random.shuffle(img_list)
for i in range(16):
    turtles[i].shape(img_list[i])

time.sleep(3)
for i in range(16):
    turtles[i].shape(default_img)

click_num = 0 # 클릭 회수 (매 2회 클릭마다 정답체)
score = 0 #점수
attempt = 0 #시도한 횟수
first_pick = ""  #첫번째 클릭한 이미지
second_pick = "" #두번째 클릭한 이미지

t.onscreenclick(play)

