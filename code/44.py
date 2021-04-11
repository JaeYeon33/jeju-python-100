# 문제 44 : 각 자리수의 합
# 사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램을 만들어 주세요.
# 예를들어
# 18234 = 1+8+2+3+4 이고 정답은 18이다.
# 3849 = 3+8+4+9 이고 정답은 24이다.

n = list(map(int, input()))
result = 0
for i in n:
    result += i

print(result)

# --------------

result = 0
for i in input():
    result += int(i)

print(result)
