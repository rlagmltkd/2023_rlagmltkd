import random


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

            if chance == 0:
                print("You Die")
            else:
                print("LEFT CHANCE : ", chance)

        if correct >= len(wordSet):  # 정답을 맞췄을때 게임 종료
            print("Alive!")
            break
