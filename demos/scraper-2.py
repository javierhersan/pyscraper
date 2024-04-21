from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

def get_cookie():
    with sync_playwright() as p:
        browser = p.chromium.launch() 
        context = browser.new_context()
        page = browser.new_page()
        page.goto("https://web.com/page")
        page.click("button[type=submit]")
        cookies = context.cookies()
        print(cookies)
        cookie_for_requests = context.cookies()[3]['value']
        browser.close()
    return cookie_for_requests

def request_with_cookie(cookie_for_request):
    cookies = dict(Cookie=f'notice_preferences=2:; notices_gdpr_prefs=0,1,2::implied,eu; euconsent-v2={cookie_for_request};')
    request = requests.get("https://web.com/page", cookies)
    return request.json()

if __name__ == '__main__':
    data = request_with_cookie(get_cookie())
    print(data['result']['pageContext']['tableData'][0])