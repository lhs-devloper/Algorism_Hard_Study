# 백준 N-Queen 9663 https://www.acmicpc.net/problem/9663
import sys  # Algorism 문제 풀 때 input보다 시간을 덜 잡아먹음


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def tracking(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if check(x):
                tracking(x + 1)


N = int(sys.stdin.readline())
row = [0] * N
result = 0
tracking(0)
print(result)
