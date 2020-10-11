#-*- coding: utf-8 -*-
'''
Logger 에서의 basicConfig 에 대해서 테스트 해보자
'''


import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    print(root)
    root.debug('hello')
    loggerA = logging.getLogger('A')
    print(loggerA)
    loggerA.debug('world')

    # 중간에 basicConfig 를 변경하면 어떻게 되는지
    logging.basicConfig(level=logging.ERROR)
    print('after set basicConfig level to logging.ERROR')
    root.debug('hello after reset basicConfig')
    loggerB = logging.getLogger('B')
    print(loggerB)
    loggerB.debug('world')

    # basicConfig 를 무시하도록 변경하면
    logging.disable(level=logging.WARNING)
    print('after disable basicConfig level to logging.WARNING')
    root.debug('hello after disable basicConfig')
    loggerC = logging.getLogger('C')
    print(loggerC)
    loggerC.error('hello')
    loggerC.debug('world')
