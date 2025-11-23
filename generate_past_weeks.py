#!/usr/bin/env python3
from pathlib import Path
from datetime import date, timedelta

# 项目根目录（本脚本所在目录）
ROOT = Path(__file__).resolve().parent

# 模板文件（就是你现在在用的 Berlin 版 template）
TEMPLATE_PATH = ROOT / "weeklog" / "week-template-berlin-zh.html" # think about change output file format -zh.html: out_path = ROOT / "weeklog" / f"week-{week_str}-zh.html"

# 需要生成的所有周一日期（闭区间：2025-09-29 ~ 2025-11-17）
START = date(2025, 9, 29)
END   = date(2025, 11, 24)


def iter_mondays(start: date, end: date):
  """从 start 到 end（包含），每隔 7 天返回一个日期。假设 start 本身就是周一。"""
  d = start
  while d <= end:
    yield d
    d += timedelta(days=7)


def generate_file_for_week(week_start: date):
  """根据模板生成某一周的 HTML 文件，并写入正确的 WEEK_START。"""
  week_str = week_start.isoformat()  # "YYYY-MM-DD"
  out_path = ROOT / "weeklog" / f"week-{week_str}-zh.html"

  if out_path.exists():
    print(f"[SKIP] {out_path.name} already exists.")
    return

  if not TEMPLATE_PATH.exists():
    raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")

  print(f"[GEN ] Creating {out_path.name} from template (WEEK_START={week_str})")

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
    print("WARNING: WEEK_START line not found in template. File still written, please check manually.")

  new_content = "\n".join(new_lines)

  # 写出新文件
  out_path.write_text(new_content, encoding="utf-8")


def main():
  print("Using template:", TEMPLATE_PATH)
  for d in iter_mondays(START, END):
    generate_file_for_week(d)
  print("Done.")


if __name__ == "__main__":
  main()