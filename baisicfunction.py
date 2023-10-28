# f(x) = 3x + 5
def tmFunction(x):
    return 3 * x + 5


print(tmFunction(5))


# 게임
# 화면뿌려주기 <- 기능
# 랜덥 값 할당받기 <- 기능
# 사용자 입력받기 <- 기능
# 값이랑 사용자 입력 비교하기 <- 기능
# 결과 출력하기 <- 기능
# 행맨
# _ _ _ _ _
# 있으면 통과, 없으면 1데카
# 데카가 n개 이상이면 out
# 1. 게임선택 -> 1. 행맨, 2. updown 3. 종료
# "행맨"
# -> 랜덤으로 단어 선정
# -> 사용자 입력을 받기
# -> 결과판단
def menuPrint():
    print("========GAME========")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("====================")


def getRandomWord():
    import random
    words = ["hang", "pretty", "apple", "ant", "water", "samsung", "MCdonalds", "f8514luent", "voca", "galaxy"]

    return words[random.randrange(0, len(words))]


hangman_input_history = []


def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if (user_input.isalpha()):
            alphabet = user_input[0].lower()
            if (alphabet in hangman_input_history):
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet


def runHangMan():
    hangman_input_history = []  # 초기화용 코드
    chance = 7
    word = getRandomWord()
    while chance > 0:
        alphabet = getHangmanInput()
        hangman_input_history.append(alphabet)
        if word.find(alphabet) != -1:
            print("CORRECT!")
            print("alive")
            print("답:", word)

            break
        else:
            chance = chance - 1
            print("LEFT CHANCE :", chance)


# 1. 모든 정답을 맞췄을때 게임이 끝나지 않음
# 맞추면 alive 출력해주고 그만하기 (break문을 사용)
# 2. 내가 맞춘 정답들이 어디에 위치해있는지 알수없음
# s _ _ s _ _ _ 출력
# print~~~() 함수를 선언해서 그 안에서 입력되었던 맞는 항목을 위치에 맞게 출력
# alphabet이 word에 속해있으면 정답이라고 알려주고, 아니면 기회를 깎기
# 8번 이상 틀렸을때는 GAME OUT
# while True :
#     if word.find(alphabet):
#         print("정답입니다")
#     else:
#         print("오답입니다")
#         Life = Life - 1
#             if Life = 0:
#                 print("GAME OUT")
# alphabet이 word에 속해있으면 정답이라고 알려주고, 아니면 기회를 깎기
# 8번 이상 틀렸을때는 GAME OUT
def runUpDown():
    import random
    answer = random.randrange(0, 10)
    chance = 3
    # 사용자가 answer 맞출때까지 반복
    # 1. 사용자에게 기회주기(3번)
    # 2. 틀렸을때 updown 출력해주기
    while chance > 0:
        user_input = int(input("값을 입력하세요 >>"))
        if user_input == answer:
            print("정답입니다!")
            break
        else:
            chance = chance - 1
            if user_input > answer:
                print("down")
            else:
                print("up")


userInput = -1
while userInput != 0:
    menuPrint()
    userInput = int(input("SELECT MENU ::: "))
    if userInput == 1:
        runHangMan()
    elif userInput == 2:
        runUpDown()
