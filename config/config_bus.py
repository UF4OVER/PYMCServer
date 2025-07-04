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
    """
    全局信号管理，不介入core模块的信号管理
    """

    serverStartSig = pyqtSignal()  # 服务器启动
    serverStopSig = pyqtSignal()  # 服务器停止

    isServerRunningSig = pyqtSignal(bool)  # 服务器运行状态

    reStartServerSig = pyqtSignal()  # 重启服务器
    addTimePlanetSig = pyqtSignal(list)  # 添加定时任务




