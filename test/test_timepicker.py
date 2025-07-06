# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 07-06 05:07
#  @FileName: test_timepicker.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout
from siui.components import SiPixLabel, SiOptionCardPlane
from siui.components.button import SiPushButtonRefactor
from siui.components.container import SiDenseContainer
from siui.components.option_card import SiOptionCardLinear
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiPushButton,
)
from siui.components.widgets.timedate import SiTimePicker
from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont

class test_timepicker(SiTimePicker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class example(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("测试")  # 设置标题

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        SiGlobal.siui.reloadStyleSheetRecursively(self)

        with self.titled_widgets_group as group:
            self.navigation_bar_h = SiOptionCardPlane(self)
            self.navigation_bar_h.setTitle("重启任务")

            self.test1 = SiTimePicker(self)

            self.test2 = SiPushButtonRefactor(self)
            self.test2.setText("替换")
            self.test2.clicked.connect(test_timepicker(self)._on_unfold_button_clicked)

            self.navigation_bar_h.body().addWidget(self.test1)
            self.navigation_bar_h.body().addWidget(self.test2)

            self.navigation_bar_h.adjustSize()
            group.addWidget(self.navigation_bar_h)
            group.adjustSize()
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)




