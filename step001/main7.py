# -*- coding: utf-8 -*-

def solution(data):
    # 2차원 배열의 길이와 주어진 데이터 차원을 변수로 할당
    from functools import reduce
    width = reduce(lambda x, y: x * y, data, 1)
    size = len(data)
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 결과를 담을 2차원 배열 생성
    result = [[0] * width for _ in range(width)]
    
    # 좌표를 보관용 list
    coord = []
    for d in data:
        y, x = 0, 0
        direction = 0
        shadow = [[0] * d for _ in range(d)]
        coord.append([y, x, direction, shadow])

    # 숫자
    num = 0

    def _2차원배열좌표계산():
        _y, _x = 0, 0
        for i in range(size):
            _y += reduce(lambda x, y: x * y, data[:i], 1) * coord[i][0]
            _x += reduce(lambda x, y: x * y, data[:i], 1) * coord[i][1]
        return _y, _x

    # 다음 좌표로 이동하기 (각각의 shadow table에 대해서)
    def _다음으로가기():
        for i in range(size):
            y, x, direction, shadow = coord[i]
            _y = y + dxy[direction][0]
            _x = x + dxy[direction][1]
            if _y < 0 or _x < 0 or _y >= data[i] or _x >= data[i] \
                or shadow[_y][_x] != 0:
                _direction = (direction + 1) % 4
                _y = y + dxy[_direction][0]
                _x = x + dxy[_direction][1]
                if _y < 0 or _x < 0 or _y >= data[i] or _x >= data[i] \
                    or shadow[_y][_x] != 0:   # 더이상 갈 곳이 없다면
                    shadow = [[0] * data[i] for _ in range(data[i])]
                    coord[i] = [0, 0, 0, shadow]
                    continue
                else:
                    coord[i] = [_y, _x, _direction, shadow]
                    return True
            else:
                coord[i] = [_y, _x, direction, shadow]
                return True

        return False

    while num < width * width:
        num += 1
        y, x = _2차원배열좌표계산()
        result[y][x] = num
        for i in range(size):
            _y, _x, _direction, _shadow = coord[i]
            _shadow[_y][_x] = num

        if not _다음으로가기():
            break

    return result


if __name__ == '__main__':
    data = [3, 2, 3]
    result = solution(data)

    for row in result:
        for col in row:
            print(f'{col:5}', end='')
        print()
