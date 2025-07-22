import asyncio
from playwright.async_api import async_playwright

async def test_ui_flow():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            executable_path="/usr/bin/google-chrome-stable"  # Adjust path as needed
        )
        page = await browser.new_page()
        await page.goto("https://example.com")
        await page.click("#login-btn")
        await page.fill("#user", "myuser")
        await page.fill("#pass", "mypassword")
        await page.click("#submit")
        await page.screenshot(path="screenshot.png")
        # Add assertions or scrape data
        await browser.close()

asyncio.run(test_ui_flow())