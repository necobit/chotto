#!/usr/bin/env python3
"""
🎨 Creative Hello World Display 🎨
様々な面白い方法でHello Worldを表示します
"""

import time
import sys
import random
import os

def clear_screen():
    """画面をクリア"""
    os.system('clear' if os.name != 'nt' else 'cls')

def wave_hello():
    """波のようにHello Worldを表示"""
    print("\n🌊 Wave Effect 🌊\n")
    text = "Hello World!"
    for offset in range(20):
        line = ""
        for i, char in enumerate(text):
            import math
            spaces = int(5 * math.sin((i + offset) * 0.5) + 5)
            line += " " * spaces + char
        print("\r" + line, end="", flush=True)
        time.sleep(0.1)
    print("\n")

def matrix_style():
    """マトリックス風に文字が降ってくる"""
    print("\n💚 Matrix Style 💚\n")
    text = "Hello World!"
    height = 15

    for frame in range(len(text) + height):
        clear_screen()
        for row in range(height):
            line = ""
            for col, char in enumerate(text):
                if frame - col == row:
                    line += char
                elif frame - col > row and frame - col < row + 3:
                    line += random.choice(['░', '▒', '▓'])
                else:
                    line += " "
            print(line)
        time.sleep(0.15)
    time.sleep(1)

def rainbow_hello():
    """虹色でHello Worldを表示"""
    print("\n🌈 Rainbow Effect 🌈\n")
    colors = [
        '\033[91m',  # 赤
        '\033[93m',  # 黄
        '\033[92m',  # 緑
        '\033[96m',  # シアン
        '\033[94m',  # 青
        '\033[95m',  # マゼンタ
    ]
    reset = '\033[0m'

    text = "Hello World!"
    for _ in range(10):
        line = ""
        for i, char in enumerate(text):
            color = colors[(i + _) % len(colors)]
            line += color + char
        print("\r" + line + reset, end="", flush=True)
        time.sleep(0.2)
    print("\n")

def typing_effect():
    """タイピング風に1文字ずつ表示"""
    print("\n⌨️  Typing Effect ⌨️\n")
    text = "Hello World!"
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.2)
    print("\n")

def explosion_effect():
    """爆発エフェクトでHello Worldを表示"""
    print("\n💥 Explosion Effect 💥\n")
    text = "Hello World!"

    # 中心から外へ広がる
    for size in range(1, 6):
        clear_screen()
        padding = " " * (20 - size * 2)
        print("\n" * (10 - size))
        print(padding + text)
        time.sleep(0.2)

    # キラキラエフェクト
    for _ in range(5):
        sparkles = ''.join(random.choice(['✨', '⭐', '🌟', ' ']) for _ in range(len(text)))
        print("\r" + sparkles, end="", flush=True)
        time.sleep(0.2)
    print("\n")

def glitch_effect():
    """グリッチエフェクト"""
    print("\n📺 Glitch Effect 📺\n")
    text = "Hello World!"
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for _ in range(15):
        glitched = ""
        for char in text:
            if random.random() < 0.3:
                glitched += random.choice(chars)
            else:
                glitched += char
        print("\r" + glitched, end="", flush=True)
        time.sleep(0.1)

    print("\r" + text + "     ")
    print()

def ascii_art_hello():
    """ASCII アートでHello Worldを表示"""
    print("\n🎨 ASCII Art 🎨\n")
    art = """
 _   _      _ _       __        __         _     _ _
| | | | ___| | | ___  \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_(_)
    """
    for line in art.split('\n'):
        print(line)
        time.sleep(0.1)

def rotate_hello():
    """回転するHello World"""
    print("\n🔄 Rotation Effect 🔄\n")
    text = "Hello World!"

    for _ in range(len(text) * 2):
        rotated = text[_ % len(text):] + text[:_ % len(text)]
        print("\r" + rotated, end="", flush=True)
        time.sleep(0.15)
    print("\n")

def menu():
    """メニューを表示"""
    clear_screen()
    print("=" * 50)
    print("🎭 Creative Hello World Collection 🎭")
    print("=" * 50)
    print("\n選択してください:")
    print("1. 🌊 Wave Effect (波エフェクト)")
    print("2. 💚 Matrix Style (マトリックス風)")
    print("3. 🌈 Rainbow Effect (虹色)")
    print("4. ⌨️  Typing Effect (タイピング風)")
    print("5. 💥 Explosion Effect (爆発エフェクト)")
    print("6. 📺 Glitch Effect (グリッチ)")
    print("7. 🎨 ASCII Art (アスキーアート)")
    print("8. 🔄 Rotation Effect (回転)")
    print("9. 🎪 All Effects (全部見る!)")
    print("0. Exit (終了)")
    print("=" * 50)

def main():
    """メインプログラム"""
    effects = {
        '1': wave_hello,
        '2': matrix_style,
        '3': rainbow_hello,
        '4': typing_effect,
        '5': explosion_effect,
        '6': glitch_effect,
        '7': ascii_art_hello,
        '8': rotate_hello,
    }

    while True:
        menu()
        choice = input("\n選択 (0-9): ").strip()

        if choice == '0':
            print("\n👋 さようなら！\n")
            break
        elif choice == '9':
            # 全てのエフェクトを順番に実行
            for key in sorted(effects.keys()):
                clear_screen()
                effects[key]()
                time.sleep(1)
        elif choice in effects:
            clear_screen()
            effects[choice]()
            input("\nEnterを押して続ける...")
        else:
            print("\n❌ 無効な選択です")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 プログラムを終了します\n")
        sys.exit(0)
