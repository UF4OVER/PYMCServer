from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-29 01:03
#  @FileName: retime_date.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import datetime
from siui.components.widgets.timedate import SiTimeSpanPicker, SiTimePicker


class ReTimeSpanPicker(SiTimeSpanPicker):
    """
    继承SiTimeSpanPicker
    添加get_time方法返回时间
    """
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def get_time(self) -> datetime.timedelta:
        return self.button.attachment().text()

class ReTimePicker(SiTimePicker):
    """

    """
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    def get_time(self) -> datetime.timedelta:
        return self.button.attachment().text()