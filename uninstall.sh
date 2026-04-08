#!/bin/bash
#
# 卸载 DeepSeek 翻译 Agent
#

SERVICES_DIR="$HOME/Library/Services"
WORKFLOW_DIR="$SERVICES_DIR/DeepSeek 翻译.workflow"
REPLACE_WORKFLOW_DIR="$SERVICES_DIR/DeepSeek 翻译替换.workflow"

echo "=== DeepSeek 翻译 Agent 卸载程序 ==="
echo ""

FOUND=false
for DIR in "$WORKFLOW_DIR" "$REPLACE_WORKFLOW_DIR"; do
    if [ -d "$DIR" ]; then
        rm -rf "$DIR"
        FOUND=true
        echo "✅ 已删除: $(basename "$DIR")"
    fi
done

if [ "$FOUND" = true ]; then
    /System/Library/CoreServices/pbs -flush 2>/dev/null || true
    echo ""
    echo "卸载完成。"
else
    echo "ℹ️  未检测到已安装的 Quick Action。"
fi

echo ""
