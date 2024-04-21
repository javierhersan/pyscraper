from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50) # headless to see the browser
    page = browser.new_page()
    page.goto("https://maps.app.goo.gl/9zgDBvgzVm8gvRw27?g_st=ic")
    page.fill("input#input-username", "admin")
    page.fill("input#input-password", "pass")
    page.click("button[type=submit]")
    page.is_visible("div.tile-body")
    html = page.inner_html("#id")
    soup = BeautifulSoup(html, "html.parser")

    total = soup.find_all("h2", {"class": "pull-right"}).text
    print(f'total_orders = {total}')