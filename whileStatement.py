# number = 0
#
# while number < 5:
#     print(number)
#     number = number + 1
#
#     print("=====메뉴=====")
#     print("1. 시작하기")
#     print("2. 종료하기")
#     print("==============")
#
#     user_input = -1
#
#     while user_input != 2:
#         user_input = int(input("값을 입력하세요 >>"))
#
# while True:
#     print("=====메뉴=====")
#     print("1. 시작하기")
#     print("2. 종료하기")
#     print("==============")

# user_input = int(input("값을 입력하세요 >>"))
# if user_input == 2:
#     break
count = 3
import random

answer = random.randrange(0, 10)
user_input = -1
# 사용자가 answer 맞출 때까지 반복
# 1. 사용자에게 기회주기(3번)
# 2. 틀렸을 때 updown 출력해주기

while user_input != answer:
    user_input = int(input("값을 입력하세요 >>"))

    if user_input == answer:
        print("정답입니다!")
        break
    elif user_input > answer:
        print("down")
        count == count - 1

    elif user_input < answer:
        print("up")
        count == count - 1

if count == 0:
    print("game over")
