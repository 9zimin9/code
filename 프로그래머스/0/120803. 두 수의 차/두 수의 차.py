def solution(num1, num2):
    if num1 < -50000 or 50000 < num1:
        raise ValueError("범위 내에 숫자를 지정해주세요.")

        
    if num2 < -50000 or 50000 < num2:
        raise ValueError("범위 내에 숫자를 지정해주세요.")
        
    return num1 - num2


print(solution(2, 3))
print(solution(100, 2))
# print(solution(60000, 2))