# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 16:40
#  @FileName: config_ini.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  :
#  @Description: 统一配置管理器类，用于读取/写入 ini 配置文件 + 路径常量定义
# -------------------------------

import configparser
from pathlib import Path
from typing import Union


class SettingsManager:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = configparser.ConfigParser()

        # 自动创建默认配置文件
        # if not self.config_path.exists():
        #     self._generate_default_config()

        self.load()

    def load(self):
        """读取配置文件"""
        self.config.read(self.config_path, encoding='utf-8')

    def get(self, section: str, option: str, fallback: Union[str, int, bool] = None) -> Union[str, int, bool]:
        if not self.config.has_section(section):
            return fallback

        if self.config.has_option(section, option):
            value = self.config.get(section, option, fallback=str(fallback))
            if value.lower() in ['true', 'false']:
                return self.config.getboolean(section, option)
            try:
                return self.config.getint(section, option)
            except ValueError:
                return value
        return fallback

    def set(self, section: str, option: str, value: Union[str, int, bool]):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, str(value))
        self._save()

    def _save(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            self.config.write(f)

    def _generate_default_config(self):
        """生成默认配置文件"""
        self.config['version'] = {
            'version': '1.0.0',
            'author': 'UF4'
        }

        self.config['runtime'] = {
            'java_path': 'C:\\Program Files\\Java\\bin\\java.exe',
            'jar_path': 'server.jar',
            'min_memory': '1G',
            'max_memory': '2G'
        }

        with open(self.config_path, 'w', encoding='utf-8') as f:
            self.config.write(f)

    # 路径配置（可用于读取资源目录）
    @property
    def base_dir(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def music_dir(self) -> Path:
        return self.base_dir / "music"

    @property
    def png_dir(self) -> Path:
        return self.base_dir / "assets"

