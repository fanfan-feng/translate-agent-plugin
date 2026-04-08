# Translate Agent

A lightweight macOS right-click translation tool powered by AI. Works with any OpenAI-compatible API.

一个轻量级的 macOS 右键翻译工具，支持任何兼容 OpenAI API 的 AI 服务。

---

## Features / 功能特点

- **Right-click to translate** — Integrates into macOS context menu via Quick Actions
  
  **右键即翻译** — 通过 macOS 快捷操作集成到右键菜单

- **Two modes** — View translation in a dialog, or replace selected text directly in input fields
  
  **两种模式** — 弹窗查看翻译结果，或在输入框中直接替换选中文本

- **Auto language detection** — Chinese ⇄ English, powered by AI
  
  **自动语言检测** — 中英文自动互译，由 AI 判断翻译方向

- **Loading state** — Visual feedback while translating, with cancel support
  
  **加载状态** — 翻译过程中有视觉反馈，支持取消

- **Zero dependencies** — Pure Python standard library, no pip install needed
  
  **零依赖** — 纯 Python 标准库，无需安装第三方包

- **Multi-provider** — Works with DeepSeek, OpenAI, Moonshot, Ollama, and any OpenAI-compatible API
  
  **多服务商** — 支持 DeepSeek、OpenAI、Moonshot、Ollama 等所有兼容 OpenAI API 的服务

## Quick Start / 快速开始

### 1. Configure / 配置

Copy the example config and fill in your API key:

复制配置模板并填写你的 API Key：

```bash
cp config.example.json config.json
```

Edit `config.json`:

```json
{
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
}
```

### 2. Install / 安装

```bash
chmod +x install.sh
./install.sh
```

### 3. Use / 使用

1. Select text in any app / 在任意应用中选中文字
2. Right-click → **Services** → **AI Translate** / 右键 → **服务** → **AI Translate**
3. Translation appears in a dialog and is copied to clipboard / 翻译结果弹窗显示并复制到剪贴板

To replace selected text directly (in editable fields):

在输入框中直接替换选中文本：

Right-click → **Services** → **AI Translate & Replace**

右键 → **服务** → **AI Translate & Replace**

## Provider Configuration / 服务商配置

The tool works with any service that provides an OpenAI-compatible chat completions API. Here are some examples:

本工具支持任何提供 OpenAI 兼容聊天补全 API 的服务。以下是一些配置示例：

### DeepSeek

```json
{
    "api_key": "sk-xxx",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
}
```

### OpenAI

```json
{
    "api_key": "sk-xxx",
    "base_url": "https://api.openai.com",
    "model": "gpt-4o-mini"
}
```

### Moonshot (Kimi)

```json
{
    "api_key": "sk-xxx",
    "base_url": "https://api.moonshot.cn",
    "model": "moonshot-v1-8k"
}
```

### Ollama (Local / 本地)

```json
{
    "api_key": "ollama",
    "base_url": "http://localhost:11434",
    "model": "qwen2.5"
}
```

### Silicon Flow

```json
{
    "api_key": "sk-xxx",
    "base_url": "https://api.siliconflow.cn",
    "model": "Qwen/Qwen2.5-7B-Instruct"
}
```

## Keyboard Shortcut / 键盘快捷键

You can assign a keyboard shortcut for faster access:

你可以设置快捷键以更快速地使用：

**System Settings → Keyboard → Keyboard Shortcuts → Services**

**系统设置 → 键盘 → 键盘快捷键 → 服务**

Find "AI Translate" and assign a shortcut (e.g. `⌘⇧T`).

找到「AI Translate」并分配快捷键（如 `⌘⇧T`）。

## Uninstall / 卸载

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Troubleshooting / 常见问题

**Q: Menu items not showing? / 右键菜单中看不到？**

Go to System Settings → Keyboard → Keyboard Shortcuts → Services, and make sure both "AI Translate" options are enabled. If still not visible, try logging out and back in.

前往 系统设置 → 键盘 → 键盘快捷键 → 服务，确认两个选项已勾选。如果仍不显示，尝试注销并重新登录。

**Q: Which apps are supported? / 支持哪些应用？**

All apps that support macOS standard text selection: Safari, Chrome, Notes, Pages, Xcode, VS Code, etc.

所有支持 macOS 标准文本选择的应用：Safari、Chrome、备忘录、Pages、Xcode、VS Code 等。

## Project Structure / 项目结构

```
translate-agent-plugin/
├── translate.py          # Core translation script / 核心翻译脚本
├── config.example.json   # Config template / 配置模板
├── config.json           # Your config (git-ignored) / 你的配置（不上传）
├── install.sh            # Installer / 安装脚本
├── uninstall.sh          # Uninstaller / 卸载脚本
├── requirements.txt      # Dependencies (none) / 依赖说明（无）
└── README.md
```

## License / 许可

MIT
