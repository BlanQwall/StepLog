#!/usr/bin/env python3
from pathlib import Path
from datetime import date, timedelta
import re
import sys

# 项目根目录（本脚本所在目录）
ROOT = Path(__file__).resolve().parent

# 模板文件：你现在用的 berlin 模板
TEMPLATE_PATH = ROOT / "weeklog" / "week-template-berlin.html"

# 输出目录
OUT_DIR = ROOT / "weeklog"


def get_next_monday(today=None):
    """返回下一个周一的 date 对象（如果今天是周一，则返回下周一）"""
    if today is None:
        today = date.today()
    # Python: Monday=0, Sunday=6
    weekday = today.weekday()
    days_ahead = (0 - weekday) % 7
    if days_ahead == 0:
        days_ahead = 7
    return today + timedelta(days=days_ahead)


def main():
    if not TEMPLATE_PATH.exists():
        print(f"Template not found: {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)

    next_monday = get_next_monday()
    week_str = next_monday.isoformat()  # "YYYY-MM-DD"

    out_path = OUT_DIR / f"week-{week_str}.html"

    if out_path.exists():
        print(f"Target file already exists: {out_path}")
        print("Overwriting it.")

    print(f"Generating new week page for {week_str} -> {out_path}")

    # 读取模板内容
    content = TEMPLATE_PATH.read_text(encoding="utf-8")

    # 按行替换：找到包含 'const WEEK_START' 的那一行，整行换成新的日期
    lines = content.splitlines()
    new_lines = []
    replaced = False
    for line in lines:
        if "const WEEK_START" in line:
            # 保留原来的缩进（行首空白）
            prefix = line[: len(line) - len(line.lstrip())]
            new_line = f'{prefix}const WEEK_START = "{week_str}";'
            new_lines.append(new_line)
            replaced = True
        else:
            new_lines.append(line)

    if not replaced:
        print("WARNING: WEEK_START line not found in template.", file=sys.stderr)

    new_content = "\n".join(new_lines)

    # 写出新文件
    out_path.write_text(new_content, encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()