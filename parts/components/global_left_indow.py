from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 21:53
#  @FileName: global_left_indow.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact :
#  @Python  :
# -------------------------------
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout
from siui.components import SiLabel, SiTitledWidgetGroup, SiCheckBox, SiDenseHContainer
from siui.components.button import SiRadioButtonR, SiSwitchRefactor
from siui.components.combobox import SiComboBox
from siui.components.container import SiDenseContainer
from siui.components.slider.slider import SiSliderH
from siui.core import SiColor
from siui.core import SiGlobal
from siui.templates.application.components.layer.global_drawer import SiLayerDrawer

class LayerLeftGlobalDrawerJVMArgs(SiLayerDrawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drawer.move(-self.drawer.width(), 0)

        self.drawer_widget_group = SiTitledWidgetGroup(self)
        self.drawer_widget_group.setSpacing(8)

        self.drawer_page.setPadding(48)
        self.drawer_page.setTitle("JVM 参数配置")
        self.drawer_page.title.setContentsMargins(32, 0, 0, 0)
        self.drawer_page.setScrollAlignment(Qt.AlignLeft)

        # GC 策略选择
        with self.drawer_widget_group as group:
            group.addTitle("垃圾回收器")

            self.gc_selector_label = SiLabel(self)
            self.gc_selector_label.setText("GC 策略")
            self.gc_selector_label.setTextColor(self.getColor(SiColor.TEXT_C))
            self.gc_selector_label.setHint("选择垃圾回收器类型，影响内存管理和性能表现")

            self.gc_selector = SiComboBox(self)
            self.gc_selector.resize(256, 32)
            self.gc_selector.addOption("Use G1GC")
            self.gc_selector.addOption("Use ZGC")
            self.gc_selector.addOption("Use ShenandoahGC")
            self.gc_selector.menu().setShowIcon(False)
            self.gc_selector.menu().setIndex(0)

            group.addWidget(self.gc_selector_label)
            group.addWidget(self.gc_selector)

        # 数值参数滑条
        with self.drawer_widget_group as group:
            group.addTitle("性能参数")

            def add_slider(label_text, min_val, max_val, default, hint_text=""):
                label = SiLabel(self)
                label.setText(label_text)
                label.setTextColor(self.getColor(SiColor.TEXT_C))
                if hint_text:
                    label.setHint(hint_text)

                slider = SiSliderH(self)
                slider.setMinimum(min_val)
                slider.setMaximum(max_val)
                slider.setValue(default, move_to=False)

                group.addWidget(label)
                group.addWidget(slider)
                group.addPlaceholder(4)

                return slider

            self.slider_xms = add_slider(
                "最小内存 Xms (MB)", 512, 16384, 4096,
                "Java 堆的最小内存大小，单位 MB"
            )
            self.slider_xmx = add_slider(
                "最大内存 Xmx (MB)", 512, 16384, 5120,
                "Java 堆的最大内存大小，单位 MB"
            )
            self.slider_g1new = add_slider(
                "G1NewSizePercent", 0, 100, 30,
                "G1 垃圾收集器新生代大小百分比"
            )
            self.slider_g1maxnew = add_slider(
                "G1MaxNewSizePercent", 0, 100, 40,
                "G1 新生代最大大小百分比"
            )
            self.slider_heap_region = add_slider(
                "G1HeapRegionSize (MB)", 1, 32, 8,
                "G1 堆区域大小，单位 MB"
            )
            self.slider_g1reserve = add_slider(
                "G1ReservePercent", 0, 100, 20,
                "G1 堆内存保留百分比"
            )
            self.slider_initiating_occupancy = add_slider(
                "InitiatingHeapOccupancyPercent", 0, 100, 15,
                "启动混合垃圾回收时的堆占用百分比阈值"
            )
            self.slider_mixed_gc_target = add_slider(
                "G1MixedGCCountTarget", 1, 16, 4,
                "G1 混合垃圾回收的目标次数"
            )
            self.slider_max_gc_pause = add_slider(
                "MaxGCPauseMillis", 10, 1000, 50,
                "最大允许的垃圾回收暂停时间，单位毫秒"
            )

        # 布尔开关参数
        with self.drawer_widget_group as group:
            group.addTitle("开关参数")

            def add_switch(label_text, default_state=True, hint_text=""):
                row = SiDenseContainer(self, QBoxLayout.LeftToRight)
                label = SiLabel(self)
                label.setText(label_text)
                label.setTextColor(self.getColor(SiColor.TEXT_C))
                label.setFixedWidth(200)
                if hint_text:
                    label.setHint(hint_text)

                switch = SiSwitchRefactor(self)
                switch.setChecked(default_state)

                row.addWidget(label)
                row.addWidget(switch)

                row.adjustSize()
                group.addWidget(row)
                return switch

            self.switch_unlock_experimental = add_switch(
                "UnlockExperimentalVMOptions", True,
                "启用实验性 JVM 参数，谨慎使用"
            )
            self.switch_parallel_ref_proc = add_switch(
                "ParallelRefProcEnabled", True,
                "开启并行引用处理，提高回收效率"
            )
            self.switch_perf_disable_mem = add_switch(
                "PerfDisableSharedMem", True,
                "禁用性能监控共享内存"
            )
            self.switch_disable_adaptive = add_switch(
                "禁用 AdaptiveSizePolicy", False,
                "关闭自适应堆大小策略"
            )
            self.switch_keep_stacktrace = add_switch(
                "保留 FastThrow 异常堆栈", False,
                "保留快速抛出异常时的堆栈信息"
            )

        group.addPlaceholder(64)
        self.drawer_page.setAttachment(self.drawer_widget_group)

    def generate_launch_command(self):
        args = []

        # 内存参数
        args.append(f"-Xms{self.slider_xms.value()}M")
        args.append(f"-Xmx{self.slider_xmx.value()}M")

        # GC 策略
        gc_map = {
            "Use G1GC": "-XX:+UseG1GC",
            "Use ZGC": "-XX:+UseZGC",
            "Use ShenandoahGC": "-XX:+UseShenandoahGC",
        }
        gc_text = self.gc_selector.currentText()
        if gc_text in gc_map:
            args.append(gc_map[gc_text])

        # 数值参数
        args += [
            f"-XX:G1NewSizePercent={self.slider_g1new.value()}",
            f"-XX:G1MaxNewSizePercent={self.slider_g1maxnew.value()}",
            f"-XX:G1HeapRegionSize={self.slider_heap_region.value()}M",
            f"-XX:G1ReservePercent={self.slider_g1reserve.value()}",
            f"-XX:InitiatingHeapOccupancyPercent={self.slider_initiating_occupancy.value()}",
            f"-XX:G1MixedGCCountTarget={self.slider_mixed_gc_target.value()}",
            f"-XX:MaxGCPauseMillis={self.slider_max_gc_pause.value()}",
        ]

        # 布尔开关参数
        def add_flag(switch: SiSwitchRefactor, flag: str, is_disable=False):
            if switch.isChecked():
                args.append(f"-XX:{'-' if is_disable else '+'}{flag}")

        add_flag(self.switch_unlock_experimental, "UnlockExperimentalVMOptions")
        add_flag(self.switch_parallel_ref_proc, "ParallelRefProcEnabled")
        add_flag(self.switch_perf_disable_mem, "PerfDisableSharedMem")
        add_flag(self.switch_disable_adaptive, "UseAdaptiveSizePolicy", is_disable=True)
        add_flag(self.switch_keep_stacktrace, "OmitStackTraceInFastThrow", is_disable=True)

        return " ".join(args)





    def setOpened(self, state):
        super().setOpened(state)
        if state:
            self.drawer.moveTo(0, 0)
        else:
            self.drawer.moveTo(-self.drawer.width(), 0)

    def reloadStyleSheet(self):
        super().reloadStyleSheet()
        self.drawer_panel.setStyleSheet(
            f"background-color: {self.getColor(SiColor.INTERFACE_BG_C)};"
            f"border-right: 1px solid {self.getColor(SiColor.INTERFACE_BG_D)}"
        )

    def showLayer(self):
        super().showLayer()
        SiGlobal.siui.windows["MAIN_WINDOW"].groups()["MAIN_INTERFACE"].moveTo(100, 0)

    def closeLayer(self):
        super().closeLayer()
        SiGlobal.siui.windows["MAIN_WINDOW"].groups()["MAIN_INTERFACE"].moveTo(0, 0)
