numbers = [1, 2, 3, 4, 5, 6, 7, 8]
strings = ["hello", "world"]

anys = [1, "hello", True, [1, 2, 3, 4]]

print(numbers[0])
print(strings[0])

print(anys[3][2])
scores = [84, -5, 65, 79, 105, 100, 91, 50, -32, 80, 54, 23, 58, 98, 64, 95, 90, 39, 84, 67, 82, 99, 91]
print(scores[3:])
print(scores[1:4])
print(scores[:3])

# 평균을 구하고 싶을때.

sum = 0
for i in scores:
    print(i)
if i > 100 or i < 0:
    print("skip", i)
   
sum = sum + i
print(sum)

average = sum / len(scores)

print("학생들의 점수 총합: ", sum)
print("학생들의 점수 평균: ", average)
