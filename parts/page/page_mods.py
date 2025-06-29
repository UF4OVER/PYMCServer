from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:47
#  @FileName: page_player.py.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact :
#  @Python  :
# -------------------------------
import os
import os

from PyQt5.QtCore import Qt
from siui.components.widgets.table import SiTableView

from siui.components import SiOptionCardPlane
from siui.components.widgets import SiLabel, SiSimpleButton
from siui.core import SiGlobal
from siui.core import Si
from PyQt5.QtCore import Qt
from siui.components import SiPixLabel
from siui.components.option_card import SiOptionCardLinear
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiPushButton,
)
from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont

from parts.components.table_manager import ModTableManager


class MCSModManagePage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("MOD管理")  # 设置标题

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        with self.titled_widgets_group as group:
            group.addTitle("")

            player_table = SiOptionCardPlane(self)
            player_table.setTitle("使用管理器的表格")

            self.mod_table = SiTableView(self)
            self.mod_table.resize(950, 450)
            self.mod_table.setManager(ModTableManager(self.mod_table))
            self.mod_table.addColumn("", 455, 80, Qt.AlignLeft| Qt.AlignVCenter)
            self.mod_table.addColumn("", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.mod_table.addColumn("", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.mod_table.addColumn("", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)

            self.mod_table.addRow(data=[["mod1", "authorA", "v1.0"], "mod2", "authorB", "v2.1"])
            self.mod_table.addRow(data=[["mod2", "authorB", "v2.1"],"mod2", "authorB", "v2.1"])
            self.mod_table.addRow(data=[["mod3", "authorC", "v0.9"],"mod2", "authorB", "v2.1"])
            self.mod_table.addRow(data=[["mod4", "authorD", "beta"],"mod2", "authorB", "v2.1"])
            self.mod_table.addRow(data=[["mod5", "authorE", "alpha"],"mod2", "authorB", "v2.1"])

            player_table.body().setAdjustWidgetsSize(True)
            player_table.body().addWidget(self.mod_table)
            player_table.body().addPlaceholder(20)
            player_table.adjustSize()

            group.addWidget(player_table)

        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)