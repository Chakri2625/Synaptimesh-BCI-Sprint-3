import subprocess

def open_browser():
    subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "https://www.google.com"
    ])


def close_browser():
    subprocess.run(
        ["taskkill", "/F", "/IM", "msedge.exe"],
        capture_output=True,
        text=True
    )