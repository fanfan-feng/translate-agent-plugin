#!/bin/bash
#
# Uninstall Translate Agent / 卸载 Translate Agent
#

SERVICES_DIR="$HOME/Library/Services"

echo "=== Translate Agent Uninstaller ==="
echo ""

FOUND=false
for NAME in "AI Translate" "AI Translate & Replace" "DeepSeek 翻译" "DeepSeek 翻译替换"; do
    DIR="$SERVICES_DIR/${NAME}.workflow"
    if [ -d "$DIR" ]; then
        rm -rf "$DIR"
        FOUND=true
        echo "✅ Removed: ${NAME}"
    fi
done

if [ "$FOUND" = true ]; then
    /System/Library/CoreServices/pbs -flush 2>/dev/null || true
    echo ""
    echo "Uninstall complete."
else
    echo "ℹ️  No installed Quick Actions found."
fi

echo ""
