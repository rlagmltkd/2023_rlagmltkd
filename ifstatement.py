score = float(input("이번 외국어 영역의 점수를 숫자만 입력해주세요."))
if score > 100 or score < 0:
    print("값을 잘못 입력한 것 같아요")

elif score >= 90:
    print("A반으로 가세요")

elif score >= 80:
    print("B반으로 가세요")

elif score >= 70:
    print("C반으로 가세요")

elif score >= 60:
    print("D반으로 가세요")

else:
    print("E반 으로 가세요")
