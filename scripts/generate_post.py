#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path

def generate_title():
return "Daily AI Insight: A Practical Quickstart"

def generate_body():
return (
"Today’s quick insight: how to bootstrap a zero-investment online business. "
"Key steps include choosing a narrow niche, creating simple content, and automating distribution."
)

def main():
date = datetime.utcnow().strftime('%Y-%m-%d')
title = generate_title()
body = generate_body()
post_dir = Path('content/posts')
post_dir.mkdir(parents=True, exist_ok=True)
slug = date + '-' + title.lower().replace(' ', '-')
md = f"""---
date: {date}

title: {title}
{body}
"""
(post_dir / f"{slug}.md").write_text(md, encoding='utf-8')
print(f"Generated post: {slug}.md")

if name == 'main':
main()

