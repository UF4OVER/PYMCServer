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

from parts.components.player_table_manager import PlayerTableManager


class MCSPlayerPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("玩家管理")  # 设置标题

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        with self.titled_widgets_group as group:
            group.addTitle("在线玩家")

            player_table = SiOptionCardPlane(self)
            player_table.setTitle("使用管理器的表格")

            self.online_player_table = SiTableView(self)
            self.online_player_table.resize(952, 250)
            self.online_player_table.setManager(PlayerTableManager(self.online_player_table))
            self.online_player_table.addColumn("排名", 32, 40, Qt.AlignRight | Qt.AlignVCenter)
            self.online_player_table.addColumn("  ", 80, 40, Qt.AlignHCenter | Qt.AlignVCenter)
            self.online_player_table.addColumn("得分", 80, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("准确度", 80, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("", 33, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("玩家用户名", 244, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("GREAT", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("OK", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("MEM", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("MISS", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addColumn("PP", 54, 40, Qt.AlignLeft | Qt.AlignVCenter)
            self.online_player_table.addRow(
                data=["#1", "S", "1,144,713", "99.36%", "China", "PrettyChicken", "514", "3", "0", "0", "114"]
            )
            self.online_player_table.addRow(
                data=["#2", "SS", "1,122,268", "100.00%", "United State", "Rick_Astley_4123", "517", "0", "0", "0", "166"]
            )
            self.online_player_table.addRow(
                data=["#3", "SS", "1,122,257", "100.00%", "Great Britain", "FishAndChips", "517", "0", "0", "0", "169"]
            )
            self.online_player_table.addRow(
                data=["#4", "SS", "1,122,190", "100.00%", "China", "SunXiaoChuan", "517", "0", "0", "0", "157"]
            )
            self.online_player_table.addRow(
                data=["#5", "S", "1,100,785", "99.12%", "China", "Sagiri_Chan", "514", "2", "1", "0", "143"]
            )

            player_table.body().setAdjustWidgetsSize(True)
            player_table.body().addWidget(self.online_player_table)
            player_table.body().addPlaceholder(12)
            player_table.adjustSize()

            group.addWidget(player_table)

        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)