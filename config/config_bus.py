# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:41
#  @FileName: config_bus.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  :
#  @Description: 全局事件总线模块，定义跨模块通信的信号
# -------------------------------

from PyQt5.QtCore import QObject, pyqtSignal


class SignalBus(QObject):
    """ Signal bus in Groove Music """
    appMessageSig = pyqtSignal(object)  # APP 发来消息
    appErrorSig = pyqtSignal(str)  # APP 发生异常
    appRestartSig = pyqtSignal()  # APP 需要重启

    serverStartSig = pyqtSignal()  # 服务器启动
    serverStopSig = pyqtSignal()  # 服务器停止


