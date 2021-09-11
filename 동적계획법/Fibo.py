# 보통의 피보나치 수열(재귀 활용)
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


# 동적계획법을 활용한 피보나치 수열
def fibo_dp(num):
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]

    return cache[num]
