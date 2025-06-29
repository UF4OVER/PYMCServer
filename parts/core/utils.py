from config import Sbus, Settings ,Logger
# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:46
#  @FileName: utils.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
from contextlib import contextmanager

from PyQt5.QtWidgets import QWidget
from siui.components.container import SiTriSectionPanelCard


@contextmanager
def createPanelCard(parent: QWidget, title: str) -> SiTriSectionPanelCard:
    card = SiTriSectionPanelCard(parent)
    card.setTitle(title)
    try:
        yield card
    finally:
        card.adjustSize()
        parent.addWidget(card)