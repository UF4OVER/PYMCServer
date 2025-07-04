import VanillaDownloader


def callback(event_type, *args):
    if event_type == "start":
        file, size = args
        print(f"开始下载: {file} ({size} bytes)")
    elif event_type == "progress":
        file, percent = args
        print(f"{file}: {percent:.1f}%")
    elif event_type == "finish":]
        file = args[0]
        print(f"完成下载: {file}")
    elif event_type == "error":
        file, error = args
        print(f"下载失败: {file} - {error}")
    elif event_type == "mirror_try":
        url, current, total = args
        print(f"尝试镜像源 {current}/{total}: {url}")
    elif event_type == "retry":
        file, attempt, max = args
        print(f"重试 {file} ({attempt}/{max})")
    elif event_type == "done":
        version = args[0]
        print(f"所有下载完成! 版本: {version}")


VanillaDownloader.download_minecraft_server("1.20.1", r"E:\python\MCServer\.minecraft", callback)
