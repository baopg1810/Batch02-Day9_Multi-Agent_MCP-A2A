"""
Task 2 - Crawl news articles about Vietnamese artists related to drug cases.

Requirements:
    1. Crawl at least 5 articles from Vietnamese news sites.
    2. Use Crawl4AI or a similar crawling library.
    3. Save output to data/landing/news/.
    4. Each article is saved as JSON with url, title, date_crawled, and content.

Install:
    pip install crawl4ai
"""

import asyncio
import json
import os
import re
from datetime import datetime
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional
from urllib.request import Request, urlopen

DATA_DIR = Path(__file__).parent.parent / "data" / "landing" / "news"


def setup_directory():
    """Create data/landing/news/ if it does not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"News directory is ready: {DATA_DIR}")


ARTICLE_URLS = [
    "https://dantri.com.vn/phap-luat/truy-to-ca-si-chi-dan-nguoi-mau-an-tay-20260402122649916.htm",
    "https://vtv.vn/phap-luat/bat-ca-si-chi-dan-nguoi-mau-an-tay-tiktoker-truc-phuong-do-lien-quan-ma-tuy-20241114123427363.htm",
    "https://dantri.com.vn/phap-luat/truy-to-dien-vien-hai-huu-tin-20221117115806098.htm",
    "https://dantri.com.vn/phap-luat/loi-ke-cua-canh-sat-dieu-tra-trong-vu-an-chau-viet-cuong-dung-toi-tru-ta-ma-dan-den-cai-chet-cua-co-gai-20-tuoi-20180311083428158.htm",
    "https://vietnamnet.vn/huu-tin-va-nhung-sao-viet-noi-tieng-ten-tin-deu-dinh-vao-ma-tuy-2029495.html",
]


class _ReadableTextParser(HTMLParser):
    """Small fallback HTML-to-text parser used when Crawl4AI is unavailable."""

    BLOCK_TAGS = {
        "article",
        "br",
        "div",
        "h1",
        "h2",
        "h3",
        "li",
        "p",
        "section",
    }
    SKIP_TAGS = {"script", "style", "noscript", "svg"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs):
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
        elif tag in self.BLOCK_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag: str):
        if tag in self.SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
        elif tag in self.BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str):
        if self._skip_depth:
            return
        text = data.strip()
        if text:
            self._parts.append(text)
            self._parts.append(" ")

    def text(self) -> str:
        raw_text = unescape("".join(self._parts))
        lines = [re.sub(r"\s+", " ", line).strip() for line in raw_text.splitlines()]
        return "\n".join(line for line in lines if len(line) > 1)


def _extract_regex(pattern: str, html: str) -> Optional[str]:
    match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    return re.sub(r"\s+", " ", unescape(match.group(1))).strip()


def _extract_title(html: str) -> str:
    return (
        _extract_regex(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', html)
        or _extract_regex(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:title["\']', html)
        or _extract_regex(r"<title[^>]*>(.*?)</title>", html)
        or "Unknown"
    )


def _strip_html(html: str) -> str:
    article_html = _extract_regex(r"<article[^>]*>(.*?)</article>", html) or html
    parser = _ReadableTextParser()
    parser.feed(article_html)
    return parser.text()


def _playwright_browser_available() -> bool:
    """Crawl4AI needs a Playwright browser; skip it if Chromium is not installed."""
    browser_root = os.environ.get("PLAYWRIGHT_BROWSERS_PATH")
    if browser_root:
        roots = [Path(browser_root)]
    elif os.name == "nt":
        local_app_data = os.environ.get("LOCALAPPDATA")
        roots = [Path(local_app_data) / "ms-playwright"] if local_app_data else []
    else:
        roots = [Path.home() / ".cache" / "ms-playwright"]

    browser_patterns = [
        "chromium-*/chrome-win*/chrome.exe",
        "chromium-*/chrome-linux/chrome",
        "chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
    ]
    return any(
        browser.exists()
        for root in roots
        for pattern in browser_patterns
        for browser in root.glob(pattern)
    )


def _fallback_crawl_with_urllib(url: str) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
            )
        },
    )
    with urlopen(request, timeout=30) as response:
        raw = response.read()
        content_type = response.headers.get("Content-Type", "")

    charset_match = re.search(r"charset=([\w-]+)", content_type, re.IGNORECASE)
    encoding = charset_match.group(1) if charset_match else "utf-8"
    html = raw.decode(encoding, errors="replace")
    title = _extract_title(html)
    content = _strip_html(html)

    return {
        "url": url,
        "title": title,
        "date_crawled": datetime.now().isoformat(timespec="seconds"),
        "content": content,
        "content_markdown": content,
        "crawler": "urllib_fallback",
    }


async def crawl_article(url: str) -> dict:
    """
    Crawl one article and return metadata plus article content.

    Returns:
        {
            "url": str,
            "title": str,
            "date_crawled": str,
            "content": str,
            "content_markdown": str
        }
    """
    try:
        if not _playwright_browser_available():
            raise RuntimeError("Playwright Chromium is not installed; using urllib fallback")

        from crawl4ai import AsyncWebCrawler

        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)

        metadata = result.metadata or {}
        content = (result.markdown or "").strip()
        title = metadata.get("title") or "Unknown"

        if len(content) < 500:
            raise ValueError("Crawl4AI returned too little content")

        return {
            "url": url,
            "title": title,
            "date_crawled": datetime.now().isoformat(timespec="seconds"),
            "content": content,
            "content_markdown": content,
            "crawler": "crawl4ai",
        }
    except Exception as exc:
        article = await asyncio.to_thread(_fallback_crawl_with_urllib, url)
        article["fallback_reason"] = str(exc)
        return article


async def crawl_all():
    """Crawl all articles in ARTICLE_URLS."""
    setup_directory()

    for i, url in enumerate(ARTICLE_URLS, 1):
        print(f"[{i}/{len(ARTICLE_URLS)}] Crawling: {url}")
        article = await crawl_article(url)

        filename = f"article_{i:02d}.json"
        filepath = DATA_DIR / filename
        filepath.write_text(json.dumps(article, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Saved: {filepath}")


if __name__ == "__main__":
    if not ARTICLE_URLS:
        print("Please fill ARTICLE_URLS before running this script.")
        print("Suggestions: VnExpress, Tuoi Tre, Thanh Nien, Dan Tri, Vietnamnet, ...")
    else:
        asyncio.run(crawl_all())
