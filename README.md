**English** | [中文](./README_CN.md)

# Translate Agent

A lightweight macOS right-click translation tool powered by AI. Works with any OpenAI-compatible API (DeepSeek, OpenAI, Moonshot, Ollama, etc.).

## Features

- **Right-click to translate** — Integrates into macOS context menu via Quick Actions
- **Two modes** — View translation in a dialog, or replace selected text directly in input fields
- **Auto language detection** — Chinese ⇄ English, powered by AI
- **Loading state** — Visual feedback while translating, with cancel support
- **Zero dependencies** — Pure Python standard library, no pip install needed
- **Multi-provider** — Works with any OpenAI-compatible API

## Quick Start

### 1. Configure

```bash
cp config.example.json config.json
```

Edit `config.json` with your API key:

```json
{
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
}
```

### 2. Install

```bash
chmod +x install.sh
./install.sh
```

### 3. Use

1. Select text in any app
2. Right-click → **Services** → **AI Translate**
3. Translation appears in a dialog and is copied to clipboard

To replace selected text directly (in editable fields):

Right-click → **Services** → **AI Translate & Replace**

## Provider Configuration

The tool works with any service that provides an OpenAI-compatible chat completions API.

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

### Ollama (Local)

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

## Install via AI Agent

If you're using an AI coding assistant (Cursor, Claude, Windsurf, etc.), copy the prompt below and send it to your agent. It will handle the entire setup for you.

<details>
<summary>📋 Click to copy the prompt</summary>

```
Help me install the Translate Agent tool on my Mac. Follow these steps:

1. Clone the repo:
   git clone https://github.com/fanfan-feng/translate-agent-plugin.git ~/translate-agent-plugin

2. Create the config file:
   cp ~/translate-agent-plugin/config.example.json ~/translate-agent-plugin/config.json

3. Ask me which AI provider I want to use (DeepSeek / OpenAI / Moonshot / Ollama / other)
   and ask me for my API key. Then write the correct base_url, model, and api_key
   into ~/translate-agent-plugin/config.json.

4. Run the install script:
   cd ~/translate-agent-plugin && chmod +x install.sh && ./install.sh

5. Verify by running a quick test:
   echo "Hello, world!" | python3 ~/translate-agent-plugin/translate.py --replace

6. Tell me the result and how to use it (right-click → Services → AI Translate).
```

</details>

## Keyboard Shortcut

Go to **System Settings → Keyboard → Keyboard Shortcuts → Services**, find "AI Translate" and assign a shortcut (e.g. `⌘⇧T`).

## Uninstall

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Troubleshooting

**Q: Menu items not showing?**

Go to System Settings → Keyboard → Keyboard Shortcuts → Services, and make sure both "AI Translate" options are enabled. If still not visible, try logging out and back in.

**Q: Which apps are supported?**

All apps that support macOS standard text selection: Safari, Chrome, Notes, Pages, Xcode, VS Code, etc.

## Project Structure

```
translate-agent-plugin/
├── translate.py          # Core translation script
├── config.example.json   # Config template
├── config.json           # Your config (git-ignored)
├── install.sh            # Installer
├── uninstall.sh          # Uninstaller
└── README.md
```

## License

MIT
