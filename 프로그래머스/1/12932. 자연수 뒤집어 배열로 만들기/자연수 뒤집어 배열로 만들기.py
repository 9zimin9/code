def solution(n):
    answer = str(n)[::-1]      # 자연수 n을 문자열로 바꿔 [::-1]로 뒤집어줌
    a_list=[]                  # 저장할 빈 리스트 변수
    for i in answer:           # 뒤집은 n 문자열을 반복
        a_list.append(int(i))  # a_list에 정수 i를 추가해 리스트를 채움
    return a_list

print(solution(12345))