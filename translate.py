#!/usr/bin/env python3
"""
Translate Agent — macOS 右键菜单翻译工具
支持任何兼容 OpenAI API 的服务（DeepSeek / OpenAI / Moonshot / Ollama 等）
自动检测语言方向：中文 ⇄ 英文
"""

import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

APP_NAME = "Translate Agent"
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        show_dialog("错误", "找不到 config.json，请先配置 API Key。\n请复制 config.example.json 为 config.json 并填写配置。")
        sys.exit(1)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_result_language(text: str) -> str:
    """根据翻译结果判断目标语言"""
    chinese_chars = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    if chinese_chars / max(len(text.strip()), 1) > 0.15:
        return "中文"
    return "英文"


def translate(text: str, config: dict) -> str:
    api_key = config.get("api_key", "")
    if not api_key:
        return "错误：请在 config.json 中填写 API Key"

    base_url = config.get("base_url", "https://api.deepseek.com")
    model = config.get("model", "deepseek-chat")

    system_prompt = (
        "你是一个专业的翻译助手。请根据以下规则翻译用户输入的文本：\n"
        "- 如果文本的主要语言是中文，请翻译为英文\n"
        "- 如果文本的主要语言是英文或其他非中文语言，请翻译为中文\n"
        "只输出翻译结果，不要添加任何解释、注释或额外内容。"
        "保持原文的格式和段落结构。"
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        "temperature": 0.3,
        "max_tokens": 4096,
    }

    url = f"{base_url.rstrip('/')}/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return f"API 请求失败 (HTTP {e.code}): {body}"
    except urllib.error.URLError as e:
        return f"网络错误: {e.reason}"
    except Exception as e:
        return f"翻译出错: {e}"


def copy_to_clipboard(text: str):
    proc = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
    proc.communicate(text.encode("utf-8"))


def show_dialog(title: str, message: str):
    escaped = message.replace("\\", "\\\\").replace('"', '\\"')
    script = (
        f'display dialog "{escaped}" '
        f'with title "{title}" '
        f'buttons {{"复制", "确定"}} default button "确定"'
    )
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
    )
    if "复制" in result.stdout:
        copy_to_clipboard(message)


def show_notification(title: str, message: str):
    escaped = message.replace("\\", "\\\\").replace('"', '\\"')
    script = (
        f'display notification "{escaped}" '
        f'with title "{title}"'
    )
    subprocess.run(["osascript", "-e", script], capture_output=True)


class LoadingDialog:
    """后台 loading 对话框，翻译完成后自动关闭。用户点取消可中止。"""

    def __init__(self):
        script = (
            f'display dialog "⏳ 正在翻译，请稍候..." '
            f'with title "{APP_NAME}" '
            f'buttons {{"取消"}} '
            f'giving up after 120'
        )
        self._proc = subprocess.Popen(
            ["osascript", "-e", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def dismiss(self):
        """关闭 loading 对话框。返回 True 表示用户已点了取消。"""
        if self._proc.poll() is not None:
            return self._proc.returncode != 0
        self._proc.terminate()
        try:
            self._proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            self._proc.kill()
        return False


def translate_with_loading(text: str, config: dict, replace_mode: bool):
    """带 loading 状态的翻译流程"""
    if replace_mode:
        show_notification(APP_NAME, "⏳ 正在翻译...")
        result = translate(text, config)
        target_lang = detect_result_language(result)
        sys.stdout.write(result)
        show_notification("翻译替换完成", f"已将选中内容替换为{target_lang}")
    else:
        loading = LoadingDialog()
        result = translate(text, config)
        cancelled = loading.dismiss()

        if cancelled:
            return

        target_lang = detect_result_language(result)
        copy_to_clipboard(result)
        show_dialog(f"翻译结果 → {target_lang}", result)


def main():
    replace_mode = "--replace" in sys.argv

    text = sys.stdin.read().strip()
    if not text:
        if not replace_mode:
            show_dialog(APP_NAME, "没有选中任何文本。")
        return

    config = load_config()
    translate_with_loading(text, config, replace_mode)


if __name__ == "__main__":
    main()
