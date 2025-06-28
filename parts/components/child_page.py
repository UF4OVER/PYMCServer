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

from siui.components import SiTitledWidgetGroup, SiOptionCardLinear, SiCircularProgressBar, SiPushButton
from siui.components.page.child_page import SiChildPage
from siui.components.widgets.timedate import SiTimeSpanPicker
from siui.core import SiGlobal

from config import Sbus
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

            restart_choose = SiTimeSpanPicker(self)
            restart_choose.adjustSize()

            restart_con.addWidget(restart_choose)
            restart_con.adjustSize()

            self.content().addWidget(restart_con)

        self.content().setAttachment(self.titled_widget_group)

        self.add_button = SiPushButton(self)
        self.add_button.resize(128, 32)
        self.add_button.attachment().setText("确定添加")
        self.add_button.clicked.connect(self.closeParentLayer)

        self.cancel_button = SiPushButton(self)
        self.cancel_button.resize(128, 32)
        self.cancel_button.attachment().setText("取消")
        self.cancel_button.clicked.connect(self.closeParentLayer)

        self.panel().addWidget(self.add_button, "right")
        self.panel().addWidget(self.cancel_button, "right")

        # todo 添加时间计划到settingpage的btu_con容器


    # load style sheet
        SiGlobal.siui.reloadStyleSheetRecursively(self)


class TimingReStartChildPage(SiChildPage):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.view().setMinimumWidth(800)
        self.content().setTitle("定时重启")
        self.content().setPadding(64)

        # page content
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            group.addTitle("兼容与提升")

            self.compatibility = SiOptionCardLinear(self)
            self.compatibility.setTitle("构建内容", "子页面与主页面的构建方式一致")
            self.compatibility.load(SiGlobal.siui.iconpack.get("ic_fluent_textbox_align_bottom_regular"))
            self.compatibility.adjustSize()

            self.improvement = SiOptionCardLinear(self)
            self.improvement.setTitle("操控区域", "子页面具有下方的固定操控区域，提供清晰明了的区域划分")
            self.improvement.load(SiGlobal.siui.iconpack.get("ic_fluent_table_bottom_row_regular"))
            self.improvement.adjustSize()

            group.addWidget(self.compatibility)
            group.addWidget(self.improvement)

        with self.titled_widget_group as group:
            group.addTitle("框架")

            self.dim_layer = SiOptionCardLinear(self)
            self.dim_layer.setTitle("背景暗化", "突出子页面内容，给用户更佳的视觉体验")
            self.dim_layer.load(SiGlobal.siui.iconpack.get("ic_fluent_position_backward_regular"))
            self.dim_layer.adjustSize()

            self.easy_closing = SiOptionCardLinear(self)
            self.easy_closing.setTitle("快速返回", "点击子页面外部区域，可快捷关闭子页面")
            self.easy_closing.load(SiGlobal.siui.iconpack.get("ic_fluent_share_close_tray_regular"))
            self.easy_closing.adjustSize()

            self.ratio_size = SiOptionCardLinear(self)
            self.ratio_size.setTitle("按比例设置尺寸", "按比例调整子控件的大小，可使用 Qt 原生方法设置最小和最大尺寸")
            self.ratio_size.load(SiGlobal.siui.iconpack.get("ic_fluent_arrow_expand_regular"))
            self.ratio_size.adjustSize()

            animation_widget = SiCircularProgressBar(self)
            animation_widget.setFixedSize(32, 32)
            animation_widget.setIndeterminate(True)

            self.animations_supporting = SiOptionCardLinear(self)
            self.animations_supporting.setTitle("动画支持", "在子页面中自由使用含动画控件")
            self.animations_supporting.load(SiGlobal.siui.iconpack.get("ic_fluent_rectangle_landscape_sparkle_regular"))
            self.animations_supporting.addWidget(animation_widget)
            self.animations_supporting.adjustSize()

            group.addWidget(self.dim_layer)
            group.addWidget(self.easy_closing)
            group.addWidget(self.ratio_size)
            group.addWidget(self.animations_supporting)
            group.addPlaceholder(48)

        self.content().setAttachment(self.titled_widget_group)

        # control panel
        self.demo_button = SiPushButton(self)
        self.demo_button.resize(128, 32)
        self.demo_button.attachment().setText("应用")
        self.demo_button.clicked.connect(self.closeParentLayer)

        self.panel().addWidget(self.demo_button, "right")

        # load style sheet
        SiGlobal.siui.reloadStyleSheetRecursively(self)
