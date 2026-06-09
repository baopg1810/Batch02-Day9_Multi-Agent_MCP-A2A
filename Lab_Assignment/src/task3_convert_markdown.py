"""
Task 3 — Convert toàn bộ file trong data/landing/ thành Markdown.

Sử dụng MarkItDown của Microsoft:
    https://github.com/microsoft/markitdown

Cài đặt:
    pip install markitdown

Hướng dẫn:
    1. Scan toàn bộ file trong data/landing/ (PDF, DOCX, JSON)
    2. Convert sang Markdown
    3. Lưu vào data/standardized/ giữ nguyên cấu trúc thư mục
"""

import json
import sys
from pathlib import Path

# Fix encoding cho Windows terminal (cp1252 -> utf-8)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from markitdown import MarkItDown

LANDING_DIR = Path(__file__).parent.parent / "data" / "landing"
OUTPUT_DIR = Path(__file__).parent.parent / "data" / "standardized"


def convert_legal_docs():
    """Convert PDF/DOCX files trong data/landing/legal/ sang markdown."""
    legal_dir = LANDING_DIR / "legal"
    output_dir = OUTPUT_DIR / "legal"
    output_dir.mkdir(parents=True, exist_ok=True)

    md = MarkItDown()

    converted = 0
    for filepath in legal_dir.iterdir():
        if filepath.suffix.lower() in (".pdf", ".docx", ".doc"):
            print(f"Converting: {filepath.name}")
            try:
                result = md.convert(str(filepath))
                output_path = output_dir / f"{filepath.stem}.md"
                output_path.write_text(result.text_content, encoding="utf-8")
                print(f"  [OK] Saved: {output_path} ({len(result.text_content)} chars)")
                converted += 1
            except Exception as e:
                print(f"  [ERR] Lỗi khi convert {filepath.name}: {e}")

    print(f"  -> Converted {converted} legal documents")
    return converted


def convert_news_articles():
    """Convert JSON crawled articles trong data/landing/news/ sang markdown."""
    news_dir = LANDING_DIR / "news"
    output_dir = OUTPUT_DIR / "news"
    output_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    for filepath in news_dir.iterdir():
        if filepath.suffix.lower() == ".json":
            print(f"Converting: {filepath.name}")
            try:
                data = json.loads(filepath.read_text(encoding="utf-8"))
                output_path = output_dir / f"{filepath.stem}.md"

                # Thêm metadata header
                header = f"# {data.get('title', 'Bài báo không có tiêu đề')}\n\n"
                header += f"**Source:** {data.get('url', 'N/A')}\n"
                header += f"**Crawled:** {data.get('date_crawled', 'N/A')}\n\n---\n\n"

                content = header + data.get("content_markdown", "")
                output_path.write_text(content, encoding="utf-8")
                print(f"  [OK] Saved: {output_path}")
                converted += 1
            except Exception as e:
                print(f"  [ERR] Loi khi convert {filepath.name}: {e}")

        elif filepath.suffix.lower() in (".html", ".md", ".txt"):
            print(f"Converting: {filepath.name}")
            try:
                # Dùng MarkItDown để convert HTML, hoặc copy thẳng nếu là .md/.txt
                if filepath.suffix.lower() == ".html":
                    md = MarkItDown()
                    result = md.convert(str(filepath))
                    text_content = result.text_content
                else:
                    text_content = filepath.read_text(encoding="utf-8")

                output_path = output_dir / f"{filepath.stem}.md"
                output_path.write_text(text_content, encoding="utf-8")
                print(f"  [OK] Saved: {output_path}")
                converted += 1
            except Exception as e:
                print(f"  [ERR] Loi khi convert {filepath.name}: {e}")

    print(f"  -> Converted {converted} news articles")
    return converted


def convert_all():
    """Convert toàn bộ files."""
    print("=" * 50)
    print("Task 3: Convert to Markdown (MarkItDown)")
    print("=" * 50)

    print("\n--- Legal Documents ---")
    n_legal = convert_legal_docs()

    print("\n--- News Articles ---")
    n_news = convert_news_articles()

    print(f"\n[Done] Tong: {n_legal} legal + {n_news} news -> Output tai: {OUTPUT_DIR}")


if __name__ == "__main__":
    convert_all()
