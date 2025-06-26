# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:38
#  @FileName: ui.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget
from siui.core import SiGlobal

from siui.templates.application.application import SiliconApplication
from parts.components.dynamic_island import DynamicIsland
from parts.components.global_left_indow import LayerLeftGlobalDrawerJVMArgs

from parts.page.page_home import MCSHomepage
from parts.page.page_mods import MCSModManagePage

from config import Settings as ST
from parts.page.page_player import MCSPlayerPage


class MySiliconApp(SiliconApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_left_global_drawer = LayerLeftGlobalDrawerJVMArgs(self)
        self.dynamic_island = DynamicIsland(self)
        self.layerMain().container_title.addWidget(self.dynamic_island)

        screen_geo = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1024, 380)
        self.resize(1300, 900)
        self.move((screen_geo.width() - self.width()) // 2, (screen_geo.height() - self.height()) // 2)
        self.layerMain().setTitle("测试标题")
        self.setWindowTitle("画廊")
        self.setWindowIcon(QIcon(f"{ST.png_dir}" + "/icon_256x256.ico"))

        self.layerMain().addPage(MCSHomepage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_home_filled"),
                                 hint="主页", side="top")
        self.layerMain().addPage(MCSModManagePage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_paint_bucket_filled"),
                                 hint="MOD", side="top")
        self.layerMain().addPage(MCSPlayerPage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_people_edit_filled"),
                                 hint="玩家", side="top")

        self.layerMain().setPage(0)

        SiGlobal.siui.reloadAllWindowsStyleSheet()

    def layerLeftGlobalDrawer(self):
        return self.layer_left_global_drawer
    def showEvent(self, event):
        super().showEvent(event)
        self.dynamic_island.move(self.size().width() // 2 - 200, 15)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.dynamic_island.move(self.size().width() // 2 - 200, 15)

