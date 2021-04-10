# 문제 41 : 소수판별
# 숫자가 주어지면 소수인지 아닌지 판별하는 프로그램을 작성해주세요.
# 소수이면 YES로, 소수가 아니면 NO로 출력해주세요.

import math

# Part 1. 2부터 N-1까지


def isPrimeNumber1(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Part 2. 에라토스테네스 접근
def isPrimeNumber2(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


# Part 3. 에라토스테네스의 체
def isPrimeNumber3(n):
    # 에라토스테니스의 체 초기화 : n개 요소에 True 설정 (소수로 간주)
    sieve = [True] * n

    # 의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:            # i가 소수인 경우
            for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


input_num = int(input('숫자를 입력하세요 : '))

print('소수판별기1 :', isPrimeNumber1(input_num))
print('소수판별기2 :', isPrimeNumber2(input_num))
print('소수판별기3 :', isPrimeNumber3(input_num))
