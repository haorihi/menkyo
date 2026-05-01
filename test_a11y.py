from playwright.sync_api import sync_playwright

def test_a11y_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.route("**/data/ch*.json", lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body="""[
                {"id": "test1", "chapter": 1, "question": "Q1", "answer": true, "explanation": "E1"}
            ]"""
        ))
        page.route("**/data/assets/global_bg.png", lambda route: route.fulfill(
            status=200, content_type="image/png", body=b""
        ))
        page.route("**/api/bookmarks", lambda route: route.fulfill(status=200, json=[]))
        page.route("**/api/flags", lambda route: route.fulfill(status=200, json=["test1"]))

        page.goto("http://localhost:8000")

        page.wait_for_selector("text=ランダム10問")

        page.evaluate("() => { const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('ランダム10問')); if(btn) btn.click(); }")

        page.wait_for_selector("text=EXERCISING")

        home_btn = page.locator("button[aria-label='ホームに戻る']").first
        home_classes = home_btn.get_attribute("class")
        print("Quiz Home Button classes:", home_classes)
        assert "focus-visible:ring-ink" in home_classes

        bookmark_btn = page.locator("button[aria-label='苦手リストに追加']").first
        bookmark_classes = bookmark_btn.get_attribute("class")
        print("Quiz Bookmark Button classes:", bookmark_classes)
        assert "focus-visible:ring-ink" in bookmark_classes
        assert bookmark_btn.get_attribute("aria-pressed") == "false"

        home_btn.evaluate("el => el.click()")
        page.wait_for_selector("text=ランダム10問")

        page.evaluate("() => { const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('要確認リスト')); if(btn) btn.click(); }")

        page.wait_for_selector("text=Review Queue")

        home_btn2 = page.locator("button[aria-label='ホームに戻る']").first
        home2_classes = home_btn2.get_attribute("class")
        print("FlagList Home Button classes:", home2_classes)
        assert "focus-visible:ring-ink" in home2_classes

        export_btn = page.locator("button[aria-label='AIレビュー用JSONをコピー']").first
        export_classes = export_btn.get_attribute("class")
        print("FlagList Export Button classes:", export_classes)
        assert "focus-visible:ring-ink" in export_classes

        browser.close()
        print("All assertions passed!")

if __name__ == "__main__":
    test_a11y_buttons()
