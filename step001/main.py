# -*- coding: utf-8 -*-
'''
Python Logging 의 기본적인 테스트
'''


import logging

if __name__ == '__main__':
    logging.critical('critical message')
    logging.error('error message')
    logging.warning('warning message')
    logging.warn('warn message')    # warn 은 deprecated 되어서 사용하지 말라고 하네.
    logging.info('info message')
    logging.debug('debug message')

