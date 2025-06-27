# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:47
#  @FileName: page_setting.py.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout
from siui.components import SiPixLabel
from siui.components.option_card import SiOptionCardLinear
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets.navigation_bar import SiNavigationBarV

from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont

from siui.components.container import SiDenseContainer, SiTriSectionRowCard

"""
- 控件选择:
SiDenseContainer 重写后的容器类，修复 https://github.com/ChinaIceF/PyQt-SiliconUI/issues/202

- 截至2025年6月28日
"""

from parts.core.utils import createPanelCard

class MCSettingPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("设置")  # 设置标题

        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        SiGlobal.siui.reloadStyleSheetRecursively(self)

        with self.titled_widgets_group as group:
            group.addTitle("定时重启")

            with createPanelCard(group, "区间指示器") as card:
                # 横向导航栏 SiNavigationBarV
                navigation_bar_v = SiNavigationBarV(card)
                # 计时重启
                navigation_bar_v.addItem("计时重启")
                # 定时重启
                navigation_bar_v.addItem("定时重启")

                navigation_bar_v.setCurrentIndex(0)
                navigation_bar_v.adjustSize()

                card.body().addWidget(navigation_bar_v)



        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)
