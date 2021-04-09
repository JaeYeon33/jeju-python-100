# 문제 20 : 몫과 나머지
# 공백으로 구분하여 두 숫자가 주어진다.
# 첫 번째 숫자로 두 번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력하시오.

data = list(map(int, input().split()))

result = data[0] // data[1]
left = data[0] % data[1]

print(result, left)
