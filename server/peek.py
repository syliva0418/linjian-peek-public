#!/usr/bin/env python3
"""掌心窗 AI/电脑端敲门脚本。"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


load_dotenv(Path(__file__).resolve().parent / ".env")
TOKEN = os.environ.get("LINJIAN_TOKEN", "").strip()
BASE = os.environ.get("LINJIAN_URL", "http://127.0.0.1:8513").rstrip("/")


def request(path: str, method: str = "GET", data: bytes | None = None, timeout: int = 10) -> bytes:
    req = urllib.request.Request(BASE + path, method=method, data=data)
    req.add_header("X-Auth-Token", TOKEN)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def latest_mtime() -> float:
    try:
        body = request("/api/latest.json")
        return float(json.loads(body.decode("utf-8")).get("mtime", 0))
    except Exception:
        return 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description="向掌心窗手机端请求一张截图")
    parser.add_argument("--wait", action="store_true", help="等待新截图上传")
    parser.add_argument("--save", default="latest.jpg", help="保存截图路径，默认 latest.jpg")
    parser.add_argument("--timeout", type=int, default=25, help="等待秒数，默认 25")
    args = parser.parse_args()

    if not TOKEN or TOKEN == "please-change-me-to-a-long-random-token":
        print("请先设置 LINJIAN_TOKEN（见 .env.example）")
        sys.exit(1)

    before = latest_mtime()
    try:
        request("/api/peek", method="POST", data=b"")
    except urllib.error.HTTPError as e:
        print(f"服务器拒绝：HTTP {e.code} {e.read().decode('utf-8', 'ignore')}")
        sys.exit(2)
    except Exception as e:
        print(f"连接服务器失败：{e}")
        sys.exit(2)

    print("已经敲门：手机端收到后会截图上传。")
    if not args.wait:
        return

    deadline = time.time() + args.timeout
    while time.time() < deadline:
        time.sleep(1)
        mt = latest_mtime()
        if mt > before:
            data = request("/api/latest")
            Path(args.save).write_bytes(data)
            print(f"新截图已保存：{args.save} ({len(data)} bytes)")
            return
    print("等待超时：手机可能未启动、无障碍未开启、服务器地址/token 不对，或 Render 正在休眠。")
    sys.exit(3)


if __name__ == "__main__":
    main()
