import re

with open('index.html', 'r') as f:
    content = f.read()

assert 'aria-label="ホームに戻る"' in content, "Missing home button aria-label"
assert 'aria-label="この問題をブックマークする"' in content, "Missing bookmark button aria-label"
assert 'aria-label="AIレビュー用JSONをコピーする"' in content, "Missing export button aria-label"
assert 'aria-hidden="true"' in content, "Missing aria-hidden"
assert 'focus-visible:ring-2' in content, "Missing focus-visible classes"

print("All accessibility enhancements verified successfully.")
