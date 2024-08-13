def solution(num1, num2):
    if not (0 <= num1 <= 100 and 0 <= num2 <= 100):
        print ("제한범위 내의 숫자를 입력해주세요.")
        return None
    
    return num1*num2

# print (solution(111, 121))