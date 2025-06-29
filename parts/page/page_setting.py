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

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout, QButtonGroup, QSizePolicy
from siui.components import SiOptionCardPlane, SiLabel
from siui.components.button import SiFlatButtonWithIndicator, SiFlatButton
from siui.components.container import SiDenseContainer, SiTriSectionRowCard
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.core import Si, SiGlobal

from config import Sbus, Logger
from parts.components.child_page import CountReStartChildPage, TimingReStartChildPage

"""
- 控件选择:

SiDenseContainer 重写后的容器类，修复 https://github.com/ChinaIceF/PyQt-SiliconUI/issues/202
SiFlatButton 扁平按钮

- 截至2025年6月28日
"""

from PyQt5.QtCore import QTimer, QDateTime
import datetime

from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QBoxLayout, QButtonGroup
from siui import *
import datetime


class MCSettingPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.restart_flag = 0  # 重启标志：0为计时，1为定时
        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("设置")

        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        SiGlobal.siui.reloadStyleSheetRecursively(self)

        def update_restart_flag(value):
            self.restart_flag = value

        with self.titled_widgets_group as group:
            self.navigation_bar_h = SiOptionCardPlane(self)
            self.navigation_bar_h.setTitle("重启任务")
            self.btu_con = SiDenseContainer(self.navigation_bar_h, QBoxLayout.LeftToRight)  # 按钮容器
            # 计时/定时选择按钮
            self.setime_restsrt_btu = SiFlatButtonWithIndicator(self.btu_con)
            self.setime_restsrt_btu.setText("定时重启")
            self.setime_restsrt_btu.setFixedHeight(40)
            self.setime_restsrt_btu.clicked.connect(lambda: update_restart_flag(1))

            self.count_restart_btu = SiFlatButtonWithIndicator(self.btu_con)
            self.count_restart_btu.setText("计时重启")
            self.count_restart_btu.setFixedHeight(40)
            self.count_restart_btu.setChecked(True)
            self.count_restart_btu.clicked.connect(lambda: update_restart_flag(0))

            add_plane_btu = SiFlatButton(self.navigation_bar_h)
            add_plane_btu.setSvgIcon(SiGlobal.siui.iconpack.get("ic_fluent_add_circle_filled"))
            add_plane_btu.setText("添加任务")
            add_plane_btu.resize(100, 32)
            add_plane_btu.clicked.connect(
                lambda:
                SiGlobal.siui.windows["MAIN_WINDOW"]
                .layerChildPage()
                .setChildPage(
                    CountReStartChildPage(self) if self.restart_flag == 0 else TimingReStartChildPage(self)
                )

            )

            self.btu_con.addWidget(self.setime_restsrt_btu)
            self.btu_con.addWidget(self.count_restart_btu)
            self.btu_con.addWidget(add_plane_btu)

            # 单选组
            btu_con_group = QButtonGroup(self)
            btu_con_group.addButton(self.setime_restsrt_btu)
            btu_con_group.addButton(self.count_restart_btu)
            btu_con_group.setExclusive(True)

            self.navigation_bar_h.header().addWidget(add_plane_btu, "right")
            self.navigation_bar_h.body().addWidget(self.btu_con)
            # 任务展示容器
            self.planet_con = SiDenseContainer(self.navigation_bar_h, QBoxLayout.TopToBottom)

            self.navigation_bar_h.body().addWidget(self.planet_con)
            self.navigation_bar_h.adjustSize()
            Sbus.addTimePlanetSig.connect(lambda x: self.addTimedTask(x))

            group.addWidget(self.navigation_bar_h)
            group.adjustSize()
        self.titled_widgets_group.addPlaceholder(64)
        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)
    def addTimedTask(self, task: list):

        # todo BUG :所有信号触发，但是task_widget不显示，
        time_str = task[1]
        delta = self.parse_time_string(time_str)
        if delta is None:
            Logger.error("时间字符串解析错误")
            return

        task_widget = SiTriSectionRowCard(self.planet_con)
        type_label = SiLabel(task_widget)
        type_label.setText(f"类型: {'定时' if task[0] == 'time' else '计时'}")
        Logger.info(f"添加任务: {'定时' if task[0] == 'time' else '计时'}")
        type_label.setTextColor("#0f6c00")

        remaining_label = SiLabel(task_widget)
        remaining_label.setTextColor("#005599")

        timer = QTimer(task_widget)
        timer.setInterval(1000)

        if task[0] == "time":
            # 定时：当前时间 + delta
            target_time = QDateTime.currentDateTime().addSecs(int(delta.total_seconds()))
            remaining_ms = QDateTime.currentDateTime().msecsTo(target_time)
        else:
            # 计时：直接用 delta
            remaining_ms = int(delta.total_seconds() * 1000)

        def update():
            nonlocal remaining_ms
            if remaining_ms <= 0:
                timer.stop()
                remaining_label.setText("正在重启...")
                Sbus.serverStartSig.emit()
                return
            seconds = remaining_ms // 1000
            h, m, s = seconds // 3600, (seconds % 3600) // 60, seconds % 60
            remaining_label.setText(f"{h:02}:{m:02}:{s:02} 后重启")
            remaining_ms -= 1000

        timer.timeout.connect(update)
        if remaining_ms > 0:
            timer.start()
            update()
        else:
            remaining_label.setText("已超时")

        Logger.info(f"{remaining_label.text()}")
        Logger.info(f"{type_label.text()}")
        task_widget.addWidget(type_label)
        task_widget.addWidget(remaining_label)
        task_widget.adjustSize()

        self.planet_con.addWidget(task_widget)
        self.planet_con.adjustSize()

        self.titled_widgets_group.adjustSize()

        Logger.debug(f"添加任务控件：{task_widget}")
        Logger.debug(f"planet_con 子控件数：{self.planet_con.layout().count()}")

    def parse_time_string(self, time_str: str) -> datetime.timedelta | None:
        try:
            parts = list(map(int, time_str.strip().split(":")))
            if len(parts) == 3:
                return datetime.timedelta(hours=parts[0], minutes=parts[1], seconds=parts[2])
            elif len(parts) == 2:
                return datetime.timedelta(minutes=parts[0], seconds=parts[1])
            elif len(parts) == 1:
                return datetime.timedelta(seconds=parts[0])
        except Exception as e:
            print(f"时间解析错误: {e}")
        return None
