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
from download import DownloaderThread, DownloadWorker
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
        self.download_manager = DownloaderThread()
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
                    self.all_versions.append([v["id"], "release"])
                case "snapshot":
                    snapshots.append(item)
                    self.all_versions.append([v["id"], "snapshot"])
                case _:
                    experiments.append(item)
                    self.all_versions.append([v["id"], "experiment"])

        with open(os.path.join(self.DATA_DIR, "releases.json"), "wb") as f:
            f.write(orjson.dumps(releases))
        with open(os.path.join(self.DATA_DIR, "snapshots.json"), "wb") as f:
            f.write(orjson.dumps(snapshots))
        with open(os.path.join(self.DATA_DIR, "experiments.json"), "wb") as f:
            f.write(orjson.dumps(experiments))

    def search_version(self, version: str, type: str):
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
            Logger.error(f"读取文件失败{e}")

        for v in version_json:
            if v["id"] == version:
                self.download_version_json(v["url"])
                Logger.infof(f"发现版本{v['id']}")

    def download_version_json(self, version_url: str):

        resp = requests.get(version_url)
        resp.raise_for_status()
        version_json = orjson.loads(resp.content)
        with open(os.path.join(self.DATA_DIR, f"{version_json['id']}.json"), "wb") as f:
            f.write(resp.content)
        self.parse_version_json(orjson.loads(resp.content))

    def parse_version_json(self, version_url):
        """
        解析版本JSON,获得服务端主jar，libraries下载地址
        """
        main_server_jar = version_url["downloads"]["server"]["url"]
        self.download_manager.addTask(DownloadWorker(main_server_jar, os.path.join(self.DATA_DIR, "server.jar")))
        for lib in version_url["libraries"]:
            if "downloads" in lib:
                self.download_manager.addTask(DownloadWorker(lib["downloads"]["artifact"]["url"], os.path.join(self.DATA_DIR, lib["downloads"]["artifact"]["path"])))




if __name__ == "__main__":
    test = Downloader()
    print(test.search_version("1.20.1", "release"))
