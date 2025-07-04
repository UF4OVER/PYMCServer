# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 07-03 12:48
#  @FileName: bmclapi2.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 3.12.11
#  @Description: 这是 BMCLAPI2 的下载模块，提供了与 BMCLAPI2 交互的功能，所有的下载任务全部由bmcl提供。
# -------------------------------

__version__ = "1.0.0"

import os

from config import Logger, Sbus
import orjson
import requests

"""
版本信息:
    http://launchermeta.mojang.com/mc/game/version_manifest.json -> https://bmclapi2.bangbang93.com/mc/game/version_manifest.json
    http://launchermeta.mojang.com/mc/game/version_manifest_v2.json -> https://bmclapi2.bangbang93.com/mc/game/version_manifest_v2.json
版本和版本JSON以及AssetsIndex:
    将版本信息内的URL中的https://launchermeta.mojang.com/ 和 https://launcher.mojang.com/ 替换为 https://bmclapi2.bangbang93.com
Assets:
    http://resources.download.minecraft.net -> https://bmclapi2.bangbang93.com/assets
Libraries:
    https://libraries.minecraft.net/ -> https://bmclapi2.bangbang93.com/maven
"""

# 官方 URL 前缀
MOJANG_LAUNCHERMETA_URL = "https://launchermeta.mojang.com"
MOJANG_LAUNCHER_URL = "https://launcher.mojang.com"
MOJANG_RESOURCES_URL = "http://resources.download.minecraft.net"
MOJANG_LIBRARIES_URL = "https://libraries.minecraft.net"

# 镜像 URL 前缀
BMCLAPI_LAUNCHERMETA_URL = "https://bmclapi2.bangbang93.com"
BMCLAPI_RESOURCES_URL = "https://bmclapi2.bangbang93.com/assets"
BMCLAPI_LIBRARIES_URL = "https://bmclapi2.bangbang93.com/maven"


class Downloader:
    def __init__(self):
        """
        """
        self.all_versions = []
        self.version_manifest = None
        self.DATA_DIR = "./data"
        os.makedirs(self.DATA_DIR, exist_ok=True)
        try:
            self.get_version_manifest()
        except requests.exceptions.ConnectionError as c:
            print(f"网络连接异常{c}")
        except Exception as e:
            print(f"下载失败{e}")

        Logger.info("获取版本清单")

    def get_version_manifest(self):
        url = f"{BMCLAPI_LAUNCHERMETA_URL}/mc/game/version_manifest_v2.json"
        resp = requests.get(url)
        resp.raise_for_status()
        self.version_manifest = orjson.loads(resp.content)

        with open(os.path.join(self.DATA_DIR, "version_manifest.json"), "wb") as f:
            f.write(resp.content)

        releases, snapshots, experiments = [], [], []

        for v in self.version_manifest["versions"]:
            item = {
                "id": v["id"],
                "url": v["url"],
                "release_time": v["releaseTime"],
                "time": v["time"]
            }
            match v["type"]:
                case "release":
                    releases.append(item)
                    self.all_versions.append([v["id"],"release"])
                case "snapshot":
                    snapshots.append(item)
                    self.all_versions.append([v["id"],"snapshot"])
                case _:
                    experiments.append(item)
                    self.all_versions.append([v["id"],"experiment"])

        with open(os.path.join(self.DATA_DIR, "releases.json"), "wb") as f:
            f.write(orjson.dumps(releases))
        with open(os.path.join(self.DATA_DIR, "snapshots.json"), "wb") as f:
            f.write(orjson.dumps(snapshots))
        with open(os.path.join(self.DATA_DIR, "experiments.json"), "wb") as f:
            f.write(orjson.dumps(experiments))

    def parse_version_json(self, version: str, type: str):
        """
        解析版本JSON,获得服务端核心，assetIndex，assets，libraries下载地址
        """
        pass
        # if type == "release":
            # version_json_url =

        # print(f"正在解析版本 {self.all_versions}")
        # version_json_url = f"{self.version_manifest["id"]['url']}"
        # resp = requests.get(version_json_url)
        # resp.raise_for_status()
        # version_json = orjson.loads(resp.content)
        # print(version_json)
        # with open(os.path.join(self.DATA_DIR, f"{version}.json"), "wb") as f:
        #     f.write(resp.content)
        #     Logger.info(f"保存版本 {version}")
    def search_version(self, version: str, type: str) -> str | None:
        print(f"正在搜索版本 {version}")
        filename = {
            "release": "releases.json",
            "snapshot": "snapshots.json"
        }.get(type, "experiments.json")

        path = os.path.join(self.DATA_DIR, filename)

        try:
            with open(path, "rb") as f:
                version_json = orjson.loads(f.read())
        except Exception as e:
            print(f"加载文件失败: {e}")
            return None

        for v in version_json:
            if v["id"] == version:
                return v["url"]

        print(f"未找到版本 {version}")
        return None


if __name__ == "__main__":
    test = Downloader()
    print(test.search_version("1.20.1","release"))


