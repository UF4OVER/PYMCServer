from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 21:53
#  @FileName: table_manager.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
from PyQt5.QtGui import QIcon
from siui.components import SiLabel, SiPixLabel
from siui.components.widgets.abstracts.table import ABCSiTabelManager, SiRow
from siui.core import GlobalFont, Si, SiColor, SiGlobal
from siui.gui import SiFont
from siui.components.button import (
    SiFlatButton,
    SiLongPressButtonRefactor,
    SiProgressPushButton,
    SiPushButtonRefactor,
    SiRadioButtonRefactor,
    SiRadioButtonWithAvatar,
    SiRadioButtonWithDescription,
    SiSwitchRefactor,
    SiToggleButtonRefactor)


class PlayerTableManager(ABCSiTabelManager):
    # #0    排名         SiLabel
    # #1    评级图片      SiPixLabel
    # #2    得分         SiLabel
    # #3    准确度       SiLabel
    # #4    国旗         SiPixLabel
    # #5    玩家用户名    SiLabel
    # #6    GREAT       SiLabel
    # #7    OK          SiLabel
    # #8    MEM         SiLabel
    # #9    MISS        SiLabel
    # #10   PP          SiLabel

    rank_dict = {
        "S": "./img/table/ranks/rank_s.png",
        "SS": "./img/table/ranks/rank_ss.png",
    }

    country_dict = {
        "China": "./img/table/flags/CN.png",
        "United State": "./img/table/flags/UM.png",
        "Great Britain": "./img/table/flags/GB.png",
    }

    def _value_read_parser(self, row_index, col_index):
        if col_index in [0, 2, 3, 5, 6, 7, 8, 9, 10]:
            return self.parent().getRowWidget(row_index)[col_index].text()

        if col_index in [1, 4]:
            path = self.parent().getRowWidget(row_index)[col_index].path()
            return list(self.country_dict.keys())[list(self.country_dict.values()).index(path)]

    def _value_write_parser(self, row_index, col_index, value):
        widget = self.parent().getRowWidget(row_index)[col_index]
        if col_index == 0:
            widget.setFont(SiFont.tokenized(GlobalFont.S_BOLD))
            widget.setTextColor(self.parent().getColor(SiColor.TEXT_B))

        if col_index == 1:
            widget.load(self.rank_dict[value])
            widget.setHint(value)

        if col_index == 2:
            widget.setTextColor(self.parent().getColor(SiColor.TEXT_B))
            if row_index == 0:
                widget.setFont(SiFont.tokenized(GlobalFont.S_BOLD))
            else:
                widget.setFont(SiFont.tokenized(GlobalFont.S_NORMAL))

        if col_index == 3:
            if value == "100.00%":
                widget.setTextColor("#B2D844")
            else:
                widget.setTextColor(self.parent().getColor(SiColor.TEXT_B))

        if col_index == 4:
            widget.load(self.country_dict[value])
            widget.setHint(value)

        if col_index == 5:
            widget.setTextColor(self.parent().getColor(SiColor.TEXT_THEME))
            widget.setHint("Click to view profile")

        if col_index in [9, 10]:
            if value == "0":
                widget.setTextColor(self.parent().getColor(SiColor.TEXT_E))
            else:
                widget.setTextColor(self.parent().getColor(SiColor.TEXT_B))
        if col_index in [6, 7, 8]:
            widget.setText("tia")

        if col_index in [0, 2, 3, 5, 9, 10]:
            widget.setText(value)

    def _widget_creator(self, col_index):
        if col_index in [0, 2, 3, 5, 9, 10]:
            label = SiLabel(self.parent())
            label.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            return label
        if col_index == 1:
            pix_label = SiPixLabel(self.parent())
            pix_label.resize(48, 24)
            pix_label.setBorderRadius(0)
            return pix_label
        if col_index == 4:
            pix_label = SiPixLabel(self.parent())
            pix_label.resize(33, 24)
            pix_label.setBorderRadius(0)
            return pix_label
        if col_index in [6, 7, 8]:  # 新增按钮列
            button = SiPushButtonRefactor(self.parent())
            button.resize(24, 24)
            return button

    def on_header_created(self, header: SiRow):
        for name in self.parent().column_names:
            new_label = SiLabel(self.parent())
            new_label.setFont(SiFont.tokenized(GlobalFont.S_BOLD))
            new_label.setTextColor(self.parent().getColor(SiColor.TEXT_D))
            new_label.setText(name)
            new_label.adjustSize()
            header.container().addWidget(new_label)

        header.container().arrangeWidgets()


class ModTableManager(ABCSiTabelManager):
    # #0    模组         SiRadioButtonWithAvatar
    # #1    删除         SiPushButtonRefactor
    # #2    禁用         SiPushButtonRefactor
    # #3    定位         SiPushButtonRefactor

    def _value_read_parser(self, row_index, col_index):
        if col_index == 1:
            #todo
            pass

        if col_index in [1, 2, 3]:
            #todo
            pass

    def _value_write_parser(self, row_index, col_index, value: list):
        widget = self.parent().getRowWidget(row_index)[col_index]
        if col_index == 0:
            widget.setFont(SiFont.tokenized(GlobalFont.S_BOLD))

            widget.setText(value[0])
            widget.setDescription(value[1])
            widget.setIcon(QIcon(value[2]))

    def _widget_creator(self, col_index):
        if col_index == 0:
            mod_choose = SiRadioButtonWithAvatar(self.parent())
            mod_choose.resize(255, 80)
            return mod_choose

        if col_index == 1:
            button = SiPushButtonRefactor(self.parent())
            button.setSvgIcon(SiGlobal.siui.iconpack.get("ic_fluent_delete_filled"))
            button.resize(30, 30)
            return button
        if col_index == 2:
            button = SiPushButtonRefactor(self.parent())
            button.setSvgIcon(SiGlobal.siui.iconpack.get("ic_fluent_prohibited_filled"))
            button.resize(30, 30)
            return button
        if col_index == 3:
            button = SiPushButtonRefactor(self.parent())
            button.setSvgIcon(SiGlobal.siui.iconpack.get("ic_fluent_folder_open_filled"))
            button.resize(30, 30)
            return button
    def on_header_created(self, header: SiRow):
        for name in self.parent().column_names:
            new_label = SiLabel(self.parent())
            new_label.setFont(SiFont.tokenized(GlobalFont.S_BOLD))
            new_label.setTextColor(self.parent().getColor(SiColor.TEXT_D))
            new_label.setText(name)
            new_label.adjustSize()
            header.container().addWidget(new_label)

        header.container().arrangeWidgets()
