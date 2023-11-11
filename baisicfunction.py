def tmpFunction(x):
    return 3 * x + 5


print(tmpFunction(5))
# 행맨
# _ _ _ _ _
# 있으면 통과, 없으면 1데카
# 데카가 n개 이상이면 out
# 게임선택 -> 1. 행맨, 2. updown, 0. 종료
# "행맨"
# -> 랜덤으로 단어 선정
# -> 사용자 입력을 받기
# -> 결과판단
import random
def menuPrint():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("==================")
def getRandomWord():
    words = ["hang", "pretty", "apple", "ant", "water", "samsung", "mcdonalds", "fluent", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]
hangman_input_history = []


def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if (user_input.isalpha()):  # 알파벳인지 확인
            alphabet = user_input[0].lower()
            if (alphabet in hangman_input_history):  # 이미 입력된 알파벳인지 확인
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet


def printPresentWords(word):
    printStr = ""
    for i in word:
        if i in hangman_input_history:
            printStr = printStr + i
        else:
            printStr = printStr + "_"
        printStr = printStr + " "
    print(printStr)


def runHangMan():
    global hangman_input_history
    # 초기화용 코드
    hangman_input_history = []
    chance = 7
    correct = 0
    word = getRandomWord()
    wordSet = set(word)
    while chance > 0:
        printPresentWords(word)
        alphabet = str(getHangmanInput())
        hangman_input_history.append(alphabet)
        if word.find(alphabet) != -1:  # alphabet이 word에 속해있으면 정답이라고 알려주고, 아니면 기회를 깎기.
            correct = correct + 1
            print("CORRECT!")
        else:
            chance = chance - 1
            print("LEFT CHANCE : ", chance)

        if correct >= len(wordSet):  # 정답을 맞췄을때 게임 종료
            print("Alive!")
            break
def runUpDown():
    answer = random.randrange(1, 10)
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