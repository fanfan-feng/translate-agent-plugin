[English](./README.md) | **中文**

# Translate Agent

一个轻量级的 macOS 右键翻译工具，支持任何兼容 OpenAI API 的 AI 服务（DeepSeek、OpenAI、Moonshot、Ollama 等）。

## 功能特点

- **右键即翻译** — 通过 macOS 快捷操作集成到右键菜单
- **两种模式** — 弹窗查看翻译结果，或在输入框中直接替换选中文本
- **自动语言检测** — 中英文自动互译，由 AI 判断翻译方向
- **加载状态** — 翻译过程中有视觉反馈，支持取消
- **零依赖** — 纯 Python 标准库，无需安装第三方包
- **多服务商** — 支持所有兼容 OpenAI API 的服务

## 快速开始

### 1. 配置

```bash
cp config.example.json config.json
```

编辑 `config.json`，填入你的 API Key：

```json
{
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
}
```

API Key 可在 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取，也可使用其他服务商。

### 2. 安装

```bash
chmod +x install.sh
./install.sh
```

### 3. 使用

1. 在任意应用中选中一段文字
2. 右键 → **服务** → **AI Translate**
3. 翻译结果弹窗显示并自动复制到剪贴板

在输入框中直接替换选中文本：

右键 → **服务** → **AI Translate & Replace**

## 服务商配置

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

### Ollama（本地部署）

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

## 键盘快捷键

前往 **系统设置 → 键盘 → 键盘快捷键 → 服务**，找到「AI Translate」并分配快捷键（如 `⌘⇧T`）。

## 卸载

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## 常见问题

**Q: 右键菜单中看不到？**

前往 系统设置 → 键盘 → 键盘快捷键 → 服务，确认两个选项已勾选。如果仍不显示，尝试注销并重新登录。

**Q: 支持哪些应用？**

所有支持 macOS 标准文本选择的应用：Safari、Chrome、备忘录、Pages、Xcode、VS Code 等。

## 项目结构

```
translate-agent-plugin/
├── translate.py          # 核心翻译脚本
├── config.example.json   # 配置模板
├── config.json           # 你的配置（不上传）
├── install.sh            # 安装脚本
├── uninstall.sh          # 卸载脚本
└── README.md
```

## 许可

MIT
