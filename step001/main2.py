# -*- coding: utf-8 -*-
'''
logging 에 포함되어 있는 몇가지 상수들과 함수들을 알아 보자.
'''


import logging


if __name__ == '__main__':
    # logging 하면서도 확인을 위해서 아직은 print 를 활용해 보자.
    print('NOTSET   : ', logging.NOTSET)
    print('CRITICAL : ', logging.CRITICAL)
    print('ERROR    : ', logging.ERROR)
    print('WARNING  : ', logging.WARNING)
    print('INFO     : ', logging.INFO)
    print('DEBUG    : ', logging.DEBUG)

    print('-' * 20)

    print('0  : ', logging.getLevelName(0))
    print('10 : ', logging.getLevelName(10))
    print('20 : ', logging.getLevelName(20))
    print('30 : ', logging.getLevelName(30))
    print('40 : ', logging.getLevelName(40))
    print('50 : ', logging.getLevelName(50))
