경우의수 = 0
백원 = input("100원의 개수를 입력하세요: ")
오백원 = input("500원의 개수를 입력하세요: ")
천원 = input("1000원의 개수를 입력하세요: ")
백원 = int(백원)
오백원 = int(오백원)
천원 = int(천원)
돈내는방법 = (백원 + 1) * (오백원 + 1) * (천원 + 1) - 1

def 금액의수 (백, 오백, 천, 결과):
    if (오백 >= 2):
        오백 = 오백 + (천 * 2)
        if(백 >= 5):
            결과 = 백 + (오백 * 5) -1
            return 결과
        elif(백 < 5):
            결과 = (백 + 1) * (오백 + 1) -1
            return 결과
    elif(오백 < 2 and 백 >=5):
        백 = 백 + (오백 * 5)
        결과 = (백 + 1) * (천 +1) -1
        return 결과
    elif(오백 < 2 and 백 < 5):
        결과 = 돈내는방법
        return 결과

결과 = 금액의수(백원, 오백원, 천원, 경우의수)
        
print(f"지불할 수 있는 방법의 수는 {돈내는방법}개 이다.")
print(f"지불할 수 있는 금액의 수는 {결과}개 이다.")
