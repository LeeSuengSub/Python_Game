import turtle as t
import time
import random

t.bgcolor("pink")
t.ht()
t.up()
num_times = int(t.textinput("숫자 기억 게임", "몇개의 숫자로 진행하시겠습니까?"))
t.write("숫자 기억하기 게임을 시작합니다.", False, "center",("bold",30))
time.sleep(3)
t.clear()


num = ""
for x in range(num_times):
    rand_num = random.randint(1,50)
    t.write(rand_num, False, "center", ("",70))
    num += str(rand_num)
    num += " "
    time.sleep(1)
    t.clear()

user_input = t.textinput("숫자 기억 게임", "기억한 숫자를 입력하세")

if user_input == num.strip(): # strip 앞에 l,s 을 적어서 왼쪽, 오른쪽 공백을 제거할수 있다. strip()만 적을시에는 왼쪽, 오른쪽 모든 공백을 제거해준다.
    t.write("정답입니다.",False,"center",("",30))
else:
    t.write("오답입니다.",False, "center", ("",30))
    t.goto(0,-50)
    t.write(f"정답은 {num}입니다.", False, "center", ("",30))
    t.goto(0,-100)
    t.write(f"입력하신 수는 {user_input}입니다.", False, "center", ("",30))
