from siui.components.popover import SiPopoverDatePicker, SiPopoverCalenderPicker, SiPopover, SiPopoverStackedWidget

from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-28 21:02
#  @FileName: child_page.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import datetime

from siui.components import SiTitledWidgetGroup, SiOptionCardLinear, SiPushButton
from siui.components.page.child_page import SiChildPage
from siui.core import SiGlobal

from config import Sbus
from parts.components.retime_date import ReTimeSpanPicker, ReTimePicker


class CountReStartChildPage(SiChildPage):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.view().setMinimumWidth(800)
        self.content().setTitle("计时重启")
        self.content().setPadding(64)

        # page content
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            group.addTitle("多长时间后重启")
            group.addPlaceholder(48)

            restart_con = SiOptionCardLinear(self)
            restart_con.setTitle("选择时间", "点击选择时间")

            restart_choose = SiPopoverDatePicker(self)
            restart_choose.adjustSize()

            restart_con.addWidget(restart_choose)
            restart_con.adjustSize()

            self.content().addWidget(restart_con)

        self.content().setAttachment(self.titled_widget_group)

        def bus_emit(type: str, time: datetime.timedelta):
            Logger.info(f"触发添加定时任务:{type} {time}")
            Sbus.addTimePlanetSig.emit([type, time])

        self.add_button = SiPushButton(self)
        self.add_button.resize(128, 32)
        self.add_button.attachment().setText("确定添加")
        self.add_button.clicked.connect(self.closeParentLayer)
        self.add_button.clicked.connect(lambda: bus_emit("count", restart_choose.date()))

        self.cancel_button = SiPushButton(self)
        self.cancel_button.resize(128, 32)
        self.cancel_button.attachment().setText("取消")
        self.cancel_button.clicked.connect(self.closeParentLayer)

        self.panel().addWidget(self.add_button, "right")
        self.panel().addWidget(self.cancel_button, "right")

        # load style sheet
        SiGlobal.siui.reloadStyleSheetRecursively(self)

class TimingReStartChildPage(SiChildPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.view().setMinimumWidth(800)
        self.content().setTitle("计划重启")
        self.content().setPadding(64)

        # 创建标题组件组
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            group.addTitle("选择重启时间")
            group.addPlaceholder(48)

            # 时间选择组件
            time_selection_card = SiOptionCardLinear(self)
            time_selection_card.setTitle("设置时间", "选择具体的时间点")

            self.time_picker = SiPopover(self)  # 假设存在ReTimePicker组件
            self.time_picker.adjustSize()

            time_selection_card.addWidget(self.time_picker)
            time_selection_card.adjustSize()

            self.content().addWidget(time_selection_card)

        self.content().setAttachment(self.titled_widget_group)

        # 按钮区域
        self.confirm_button = SiPushButton(self)
        self.confirm_button.resize(128, 32)
        self.confirm_button.attachment().setText("确认")
        self.confirm_button.clicked.connect(self.closeParentLayer)
        self.confirm_button.clicked.connect(self.emit_scheduled_time)

        self.cancel_button = SiPushButton(self)
        self.cancel_button.resize(128, 32)
        self.cancel_button.attachment().setText("取消")
        self.cancel_button.clicked.connect(self.closeParentLayer)

        self.panel().addWidget(self.confirm_button, "right")
        self.panel().addWidget(self.cancel_button, "right")

        SiGlobal.siui.reloadStyleSheetRecursively(self)

    def emit_scheduled_time(self):
        """触发计划时间信号"""
        Sbus.addTimePlanetSig.emit(["time", self.time_picker.get_time()])
