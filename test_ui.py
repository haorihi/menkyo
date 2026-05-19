from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Mocking API calls and JSON to prevent hanging since there's no backend
    page.route("**/data/ch*.json", lambda route: route.fulfill(status=200, content_type="application/json", body='[{"id": "mock_id", "chapter": 1, "question": "Mock Question", "answer": true, "explanation": "Mock Explanation"}]'))
    page.route("**/data/assets/global_bg.png", lambda route: route.fulfill(status=200, content_type="image/png", body=b""))
    page.route("**/api/bookmarks", lambda route: route.fulfill(status=200, content_type="application/json", body="[]"))
    page.route("**/api/flags", lambda route: route.fulfill(status=200, content_type="application/json", body="[]"))

    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(2000)

    # 1. Start the random 10 quiz to enter the quiz view
    page.evaluate('''() => {
        const btn = Array.from(document.querySelectorAll('button')).find(el => el.textContent.includes('ランダム10問'));
        if (btn) btn.click();
    }''')
    page.wait_for_timeout(2000)

    # 2. Simulate Tab to focus the Home button
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)

    # 3. Simulate Tab to focus the Bookmark button
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)

    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/videos")
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
