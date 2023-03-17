#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import sys
from logging.handlers import RotatingFileHandler

# 获取可执行文件的路径
if getattr(sys, 'frozen', False):
    # 如果是打包后的 exe 文件，获取可执行文件的路径
    app_dir = os.path.dirname(sys.executable)
else:
    # 如果是源代码，获取脚本文件所在的目录
    app_dir = os.path.dirname(os.path.abspath(__file__))

# 创建 log 文件夹
log_dir = os.path.join(app_dir, 'log')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# 配置 logging 模块
log_file = os.path.join(log_dir, 'DataQuery.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建 RotatingFileHandler，设置文件名、文件大小、保留文件数量和编码方式
# handler = RotatingFileHandler('example.log', maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5,
                              encoding='utf-8')

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

# 添加处理器到 logger
logger.addHandler(handler)

# 输出日志信息
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

logger.info('初始化日志...')
