from config import Sbus, Settings, Logger  # -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 06-25 19:39
#  @FileName: setup.py.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------

from cx_Freeze import setup, Executable

# 设置 GUI 基础
base = "Win32GUI"


def build_exe_cx_freeze():
    build_exe_options = {  # 构建选项
        "packages":  # 包
            [
                "PyQt5.QtCore",
                "PyQt5.QtGui",
                "PyQt5.QtWidgets",
                "siui",
                "parts",
                "config",
                "numpy"
            ],
        "include_files":  # 包含文件
            [
                "assets"
             ],
        "excludes":  # 排除文件/包
            [
                "matplotlib",
                "backports",
                "PIL",
                "lib2to3",
                "setuptools",
                "tkinter",
                "unittest",
                "email",
                "cryptography",
                "pydoc",
                "numpy"
            ],
        "optimize": 2
    }

    setup(
        name='PYMCS',
        version="0.0.1",
        url='https://github.com/UF4OVER',
        license='GPLv3',
        author='UF4',
        author_email='heping@uf4.top',
        description='MCSERVER',
        options={"build_exe": build_exe_options},
        executables=[
            Executable(
                script="start.py",
                target_name="YuC",
                base=base,
                icon="assets/icon_256x256.ico"
            )
        ]
    )


if __name__ == '__main__':
    build_exe_cx_freeze()
