import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
from bs4 import BeautifulSoup

# Run 'playwright codegen' to generate playwright code with user actions

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://maps.app.goo.gl/9zgDBvgzVm8gvRw27?g_st=ic")

    page.mouse.wheel(0,4000)
    
    cookie_modal = page.locator('Aceptar todo')
    if (cookie_modal.is_visible): 
        print("Accept cookies is visible")
        page.get_by_role("button", name="Aceptar todo").click()
    
    page.mouse.wheel(0,4000)
    page.get_by_label("Sushi Koi", exact=True).click()

    page.mouse.wheel(0,4000)
    page.get_by_label("Reseñas de Sushi Koi").click()

    reviews = page.locator("div[aria-label='Sushi Koi']")
    print(reviews)
    html = page.inner_html("div[aria-label='Sushi Koi']")
    print(html)

    with open("./demos/output/output.html", "w", encoding='utf-8') as text_file:
        text_file.write(html)
    # page.mouse.wheel(0,4000)
    # page.get_by_label("Más reseñas (125)").click()

    

    time.sleep(2)
    page.mouse.wheel(0,20000)
    time.sleep(2)


    # time.sleep(30)
    # html = page.inner_html("#id")
    # soup = BeautifulSoup(html, "html.parser")

    # total = soup.find_all("h2", {"class": "pull-right"}).text

    # page.get_by_label("Más reseñas (125)").click()
    # page.goto("https://www.google.com/maps/place/Sushi+Koi/@40.4628757,-3.6798831,14z/data=!3m1!5s0xd422f25dee4a063:0xe8c76feac096860c!4m12!1m2!2m1!1sSushi+Koi,+C.+de+Arturo+Soria,+126,+128,+Cdad.+Lineal,+28043+Madrid!3m8!1s0xd422f25e714b889:0x97c150184bdd5dea!8m2!3d40.4503103!4d-3.650609!9m1!1b1!15sCkNTdXNoaSBLb2ksIEMuIGRlIEFydHVybyBTb3JpYSwgMTI2LCAxMjgsIENkYWQuIExpbmVhbCwgMjgwNDMgTWFkcmlkWj4iPHN1c2hpIGtvaSBjIGRlIGFydHVybyBzb3JpYSAxMjYgMTI4IGNkYWQgbGluZWFsIDI4MDQzIG1hZHJpZJIBEHN1c2hpX3Jlc3RhdXJhbnSaASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVTnZMVTVVVWtwbkVBReABAA!16s%2Fg%2F1z44bcvzj?entry=ttu")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)