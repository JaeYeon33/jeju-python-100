# 문제 50 : 버블정렬 구하기
# 버블정렬은 두 인접한 원소를 검사하여 정렬하는 방법을 말한다. 시간 복잡도는 느리지만 코드가 단순하기 때문에 자주 사용된다.

def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end=" ")


n = int(input())
data = list(map(int, input().split()))
bubble(n, data)
