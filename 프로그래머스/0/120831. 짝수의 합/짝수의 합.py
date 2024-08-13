def solution(n):
    answer =0                # 변수를 0으로 만들어줌
    for i in range(2,n+1,2): # 2부터 n까지 짝수를 반복, 2씩 증가 하도록
        answer += i          # i값을 변수에 더해준다

    return answer