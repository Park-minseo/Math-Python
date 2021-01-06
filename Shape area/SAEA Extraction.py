x = []
y = []
계산가능도형 = ["삼각형", "원"]
def 삼각형(x1, y1, x2, y2, x3, y3):
    넓이 = abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1  - x3 * y2 - x1 * y3) * 0.5
    return 넓이

print("계산 가능 도형 : 삼각형, 원")
도형=input("넓이를 계산할 도형을 입력해주세요 :")

if 도형 != "삼각형" and 도형 != "원":
    print("지원되지 않는 도형입니다.")
if 도형 == "삼각형":
    for a in range(3):
        b = a+1
        x.append(float(input("{}번째 점의 x좌표를 입력해주세요: ".format(b))))
        y.append(float(input("{}번째 점의 y좌표를 입력해주세요: ".format(b))))
    print("삼각형의 넓이는 {} 입니다.".format(삼각형(x[0], y[0], x[1], y[1], x[2], y[2])))
if 도형 == "원":
    반지름=float(input("반지름을 입력해주세요: "))
    print("원의 넓이는 {}π 입니다. ".format(반지름 * 반지름))
