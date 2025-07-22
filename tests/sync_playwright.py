from playwright.sync_api import sync_playwright

def test_ui_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            executable_path="/usr/bin/google-chrome-stable"  # Adjust path as needed
        )
        page = browser.new_page()
        page.goto("https://example.com")
        page.click("#login-btn")
        page.fill("#user", "myuser")
        page.fill("#pass", "mypassword")
        page.click("#submit")
        page.screenshot(path="screenshot.png")
        # Add assertions or scrape data
        browser.close()

if __name__ == "__main__":
    test_ui_flow()