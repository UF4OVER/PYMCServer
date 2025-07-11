# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 17:41
#  @FileName: __init__.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
from pathlib import Path

from .config_bus import SignalBus as _SignalBus
from .config_ini import SettingsManager as _SettingsManager
from .config_log import logger as _logger

INI_PATH = Path(__file__).resolve().parent / "config.ini"
if not INI_PATH.exists():
    INI_PATH.touch()

Settings = _SettingsManager(INI_PATH)
Sbus = _SignalBus()
Logger = _logger


ADMIN_NAME = Settings.get("name", "admin_name")
SERVER_NAME = Settings.get("name", "server_name")
SERVER_VERSION = Settings.get("name", "server_version")
SOFTWARE_VERSION = Settings.get("name", "software_version")

