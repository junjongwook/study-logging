# -*- coding: utf-8 -*-

def solution(data):
    # 최종 결과인 2차원 배열의 width 를 계산
    from functools import reduce
    width = reduce(lambda x, y : x * y, data, 1)  # [3, 2, 3] 으로 입력이 들어오면 3 * 2 * 3 의 결과를 반환

    # 1 부터 마지막 숫자까지의 1차원 배열 생성
    result = list(range(1, width ** 2 + 1))

    # 단계별로 달팽이 - spiral 형태로 변형
    for _d in data:
        size = len(result)
        temp = []
        for start in range(0, size, _d ** 2):
            temp2 = result[start:start + _d ** 2]   # 달팽이로 만들 대상 추출 
            temp3 = 달팽이(temp2, _d)
            temp.append(temp3)
        result = temp

    # 작업 때문에 만들어진 바깥의 배열은 제거
    while True:         
        if len(result) == 1:
            result = result[0]
        else:
            break

    data2 = []
    curr = [0] * len(data) * 2
    for _d in data:
        data2.append(_d)
        data2.append(_d)

    # 다차원 배열을 1차원 배열로 변경한다.
    temp = [0] * (width ** 2)
    while curr is not None:
        위치 = 직렬화(curr, data)        # 해당 좌표가 직렬화 했을때 위치 지점 찾기
        temp[위치] = 다차원요소(result, curr)  # 해당 좌표의 값을 찾아서 해당 위치에 넣기
        curr = 다음좌표값(curr, data2)   # 다차원의 좌표를 순차적으로 증가해서 순회하기

    # 1차원 배열을 2차원 배열로 변환
    result = []
    for start in range(0, len(temp), width):
        result.append(temp[start:start+width])

    return result


def 달팽이(numbers, width):
    result = [[None] * width for _ in range(width)] # 2차원 배열을 만들어서 기본값으로 None 을 등록
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]        # 움직이는 방향의 순서를 정의한다.
    # dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]        # 움직이는 방향의 순서를 정의한다.
    arrow = 0
    h, w = 0, 0
    for num in numbers:
        result[h][w] = num
        _h = h + dxy[arrow][0]
        _w = w + dxy[arrow][1]
        if 벽(_h, _w, width) or result[_h][_w] is not None:
            arrow = (arrow + 1) % 4
            h = h + dxy[arrow][0]
            w = w + dxy[arrow][1]
        else:
            h = _h
            w = _w

    return result


def 벽(h, w, width):
    if h < 0 or w < 0:
        return True
    if h >= width or w >= width:
        return True

    return False


def 다차원요소(data, cord):
    temp = data
    for i, c in enumerate(reversed(cord)):
        temp = temp[c]
        # if isinstance(temp, int):
        #     break

    return temp


def 다음좌표값(curr, end):
    result = curr[:]
    for i in range(len(curr)):
        temp = curr[i]
        temp = temp + 1
        if temp < end[i]:
            result[i] = temp
            return result
        else:
            result[i] = 0

    return None


def 직렬화(curr, data):
    from functools import reduce
    width = reduce(lambda x, y : x * y, data, 1)
    base = 1
    result = 0
    for i, e in enumerate(data):
        result += curr[i * 2] * base
        result += curr[i * 2 + 1] * width * base
        base *= e

    return result

if __name__ == '__main__':
    result = solution([3, 2, 3])
    # result = solution([3, 2])
    # result = solution([3])

    for row in result:
        for col in row:
            print(f'{col:5}', end='')
        print()