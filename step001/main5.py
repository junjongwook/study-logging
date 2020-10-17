def solution(n):
    temp = []
    for _ in range(n*2 -1):
        temp.append(['G'] * n)

    for i in range(n-1, 0, -1):
        for j in range(i):
            temp[n - i - 1][n-j-1] = 'B'
            temp[n + i - 1][j] = 'B'

    result = []
    for t in temp:
        result.append("".join(t))

    return result


if __name__ == '__main__':
    print(solution(2))
    print(solution(3))
    print(solution(4))