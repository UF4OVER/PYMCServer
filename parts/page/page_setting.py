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
from PyQt5.QtWidgets import QBoxLayout, QButtonGroup
from siui.components import SiPixLabel, SiOptionCardPlane
from siui.components.button import SiFlatButtonWithIndicator, SiFlatButton
from siui.components.option_card import SiOptionCardLinear
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets.navigation_bar import SiNavigationBarV, SiNavigationBarH

from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont

from siui.components.container import SiDenseContainer, SiTriSectionRowCard

from parts.components.child_page import CountReStartChildPage, TimingReStartChildPage

from config import Sbus, Logger

"""
- 控件选择:

SiDenseContainer 重写后的容器类，修复 https://github.com/ChinaIceF/PyQt-SiliconUI/issues/202
SiFlatButton 扁平按钮

- 截至2025年6月28日
"""

from parts.core.utils import createPanelCard


class MCSettingPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._solt()
        self.restart_flag = 0  # 重启标志   0: 计时重启，1: 定时重启
        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("设置")  # 设置标题

        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        SiGlobal.siui.reloadStyleSheetRecursively(self)

        def update_restart_flag(value):
            self.restart_flag = value

        with self.titled_widgets_group as group:
            self.navigation_bar_h = SiOptionCardPlane(self)
            self.navigation_bar_h.setTitle("重启任务")
            self.btu_con = SiDenseContainer(self.navigation_bar_h, QBoxLayout.LeftToRight)
            # 定时重启
            self.setime_restsrt_btu = SiFlatButtonWithIndicator(self)
            self.setime_restsrt_btu.setText("定时重启")
            self.setime_restsrt_btu.setFixedHeight(40)
            self.setime_restsrt_btu.clicked.connect(
                lambda: update_restart_flag(1)
            )

            # 计时重启
            self.count_restart_btu = SiFlatButtonWithIndicator(self)
            self.count_restart_btu.setText("计时重启")
            self.count_restart_btu.setFixedHeight(40)
            self.count_restart_btu.setChecked(True)
            self.count_restart_btu.clicked.connect(
                lambda: update_restart_flag(0)
            )

            add_plane_btu = SiFlatButton(self)
            add_plane_btu.setSvgIcon(SiGlobal.siui.iconpack.get("ic_fluent_add_circle_filled"))
            add_plane_btu.setText("添加任务")
            add_plane_btu.resize(100, 32)
            add_plane_btu.clicked.connect(
                lambda:
                SiGlobal.siui.windows["MAIN_WINDOW"].
                layerChildPage().
                setChildPage(CountReStartChildPage(self))

                if self.restart_flag == 0 else

                SiGlobal.siui.windows["MAIN_WINDOW"].
                layerChildPage().
                setChildPage(TimingReStartChildPage(self)))

            self.btu_con.addWidget(self.setime_restsrt_btu)
            self.btu_con.addWidget(self.count_restart_btu)

            btu_con_group = QButtonGroup(self)
            btu_con_group.addButton(self.setime_restsrt_btu)
            btu_con_group.addButton(self.count_restart_btu)
            btu_con_group.setExclusive(True)

            self.navigation_bar_h.header().addWidget(add_plane_btu, "right")

            self.navigation_bar_h.body().addWidget(self.btu_con)
            self.navigation_bar_h.body().addPlaceholder(12)
            self.navigation_bar_h.adjustSize()

            group.addWidget(self.navigation_bar_h)

        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)
    def _solt(self):
        Sbus.addTimePlanetSig.connect(lambda x: self.addTimePlanet(x))

    def addTimePlanet(self, a0:list):
        Logger.info(f"添加时间计划{list(a0)}")