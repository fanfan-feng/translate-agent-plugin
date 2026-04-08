# DeepSeek 翻译 Agent

一个轻量级的 macOS 右键翻译工具，通过 DeepSeek API 实现智能翻译。

选中任意文字 → 右键 → 服务 → **DeepSeek 翻译**，即可获得翻译结果。

## 功能特点

- 自动检测语言方向：中文 → 英文，其他语言 → 中文
- 翻译结果弹窗显示，并自动复制到剪贴板
- 零依赖，仅使用 Python 标准库
- 一键安装/卸载

## 快速开始

### 1. 配置 API Key

编辑 `config.json`，填入你的 DeepSeek API Key：

```json
{
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
}
```

API Key 可在 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取。

### 2. 安装到右键菜单

```bash
chmod +x install.sh
./install.sh
```

### 3. 使用

1. 在任意应用中选中一段文字
2. 右键点击 → **服务** → **DeepSeek 翻译**
3. 等待翻译完成，结果会弹窗显示并自动复制到剪贴板

### 4. 设置快捷键（可选）

前往 **系统设置 → 键盘 → 键盘快捷键 → 服务 → 文本**，找到「DeepSeek 翻译」，为其分配一个快捷键（如 `⌘+⇧+T`）。

## 卸载

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## 配置说明

| 字段 | 说明 | 默认值 |
|------|------|--------|
| `api_key` | DeepSeek API Key | （必填） |
| `base_url` | API 接口地址 | `https://api.deepseek.com` |
| `model` | 模型名称 | `deepseek-chat` |

## 常见问题

**Q: 右键菜单中没有「DeepSeek 翻译」选项？**

前往 系统设置 → 键盘 → 键盘快捷键 → 服务，确认「DeepSeek 翻译」已勾选。如果仍不显示，尝试注销并重新登录。

**Q: 可以使用其他兼容 OpenAI API 的服务吗？**

可以。修改 `config.json` 中的 `base_url` 和 `model` 即可，例如使用 OpenAI、Moonshot 等。

**Q: 支持哪些应用？**

支持所有遵循 macOS 标准文本选择的应用，如 Safari、Chrome、备忘录、Pages、Xcode 等。

## 项目结构

```
translate-agent-plugin/
├── translate.py       # 核心翻译脚本
├── config.json        # API 配置文件
├── install.sh         # 安装脚本
├── uninstall.sh       # 卸载脚本
├── requirements.txt   # 依赖说明
└── README.md          # 本文件
```
