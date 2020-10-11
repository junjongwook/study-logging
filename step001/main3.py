# -*- coding: utf-8 -*-
'''
Log Level 을 지정해서 출력 대상을 지정할 수 있다.
logging 을 Logger 를 따로 생성하지 않고 바로 사용하면 내부적으로 root 라는 property 에 대응되어 있는
Root Logger 를 사용한다.
'''

import logging
from logging import StreamHandler


if __name__ == '__main__':
    root = logging.root

    print('before set log level--------')
    print(root)
    root.warning('warning message before set log level')
    root.info('info message before set log level')
    root.debug('debug message before set log level')

    root.setLevel(logging.DEBUG)

    print('after set log level---------')
    print(root)
    print('Effective log level : ', logging.getLevelName(root.getEffectiveLevel()))
    root.warning('warning message after set log level')
    root.info('info message after set log level')
    root.debug('debug message after set log level')

    handler = StreamHandler()
    print(root.handlers)
    print('after add handler----------')
    root.addHandler(handler)
    print(root.handlers)
    print(handler)
    root.warning('warning message after add log handler')
    root.info('info message after add log handler')
    root.debug('debug message after add log handler')


