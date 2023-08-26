number = 0

while number < 5:
    print(number)
    number = number + 1

    print("=====메뉴=====")
    print("1. 시작하기")
    print("2. 종료하기")
    print("==============")

    user_input = -1

    while user_input != 2:
        user_input = int(input("값을 입력하세요 >>"))

while True:
    print("=====메뉴=====")
    print("1. 시작하기")
    print("2. 종료하기")
    print("==============")

    user_input = int(input("값을 입력하세요 >>"))
    if user_input == 2:
        break
