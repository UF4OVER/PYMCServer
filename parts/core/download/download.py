# -*- coding: utf-8 -*-
# -------------------------------
#  @Project : MCServer
#  @Time    : 2025 - 07-03 12:56
#  @FileName: download.py
#  @Software: PyCharm 2024.1.6 (Professional Edition)
#  @System  : Windows 11 23H2
#  @Author  : 33974
#  @Contact : 
#  @Python  : 
# -------------------------------
import requests
from PyQt5.QtCore import QThread, pyqtSignal, QObject

from config import Logger


class DownloadWorker(QObject):
    progress = pyqtSignal(str, int)    # url, percent
    finished = pyqtSignal(str)          # url
    error = pyqtSignal(str, str)        # url, errmsg
    def __init__(self, url, file_path, sha1):
        super().__init__()
        self.url = url
        self.file_path = file_path
        self.sha1 = sha1
        self._is_cancelled = False
    def run(self):
        try:
            with requests.get(self.url, stream=True, timeout=10) as r:
                r.raise_for_status()
                total = int(r.headers.get("content-length", 0))
                with open(self.file_path, "wb") as f:
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=8192):  # 8kb
                        if self._is_cancelled:
                            return
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            percent = int(downloaded * 100 / total)
                            self.progress.emit(self.url, percent)
            self.finished.emit(self.url)
        except Exception as e:
            self.error.emit(self.url, str(e))

    def __id__(self):
        return id(self)
    def cancel(self):
        self._is_cancelled = True

class DownloaderThread(QObject):
    def __init__(self):
        super().__init__()
        self.threads = []  # 用于保存所有线程

    def addTask(self, task: DownloadWorker):
        thread = QThread()
        task.moveToThread(thread)
        Logger.info(f"启动下载任务: {task.url},任务ID:{task.__id__()}")
        thread.started.connect(task.run)

        # task.progress.connect(self.onProgress)
        # task.finished.connect(self.onFinished)
        # task.error.connect(self.onError)

        task.finished.connect(thread.quit)
        task.finished.connect(task.deleteLater)
        thread.finished.connect(thread.deleteLater)

        thread.start()

        # 保存线程引用，防止被销毁
        self.threads.append(thread)
