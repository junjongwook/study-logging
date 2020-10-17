def solution(data, seed):
    result = []

    from functools import cmp_to_key
    def custom_order(x, y):
        x_length = len(x)
        y_length = len(y)
        length = min(x_length, y_length)
        for i in range(length):
            if seed.index(x[i]) < seed.index(y[i]):
                return -1
            elif seed.index(x[i]) > seed.index(y[i]):
                return 1

        if y_length > length:
            return -1
        elif x_length > length:
            return 1

        return 0

    result = sorted(data, key=cmp_to_key(custom_order))

    return result

if __name__ == '__main__':
    data = ['pychon', 'c',  'java', 'basic', 'cobol']
    seed = 'jgcewbqsliaukpoyvmxfdrznht'
    result = solution(data, seed)
    print(result)