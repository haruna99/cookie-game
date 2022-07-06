from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element("css selector", "#cookie")
costs = driver.find_elements("css selector", "#store b")
costs.pop()

[cursor, grandma, factory, mine, shipment, alchemy, portal, machine] = \
    [int(cost.text.split("-")[1].strip().replace(",", "")) for cost in costs]


def purchase():
    money = int(driver.find_element("css selector", "#money").text.replace(",", ""))
    if money >= machine:
        driver.find_element("css selector", "#buyTime machine").click()
    elif money >= portal:
        driver.find_element("css selector", "#buyPortal").click()
    elif money >= alchemy:
        driver.find_element("css selector", "#buyAlchemy lab").click()
    elif money >= shipment:
        driver.find_element("css selector", "#buyShipment").click()
    elif money >= mine:
        driver.find_element("css selector", "#buyMine").click()
    elif money >= factory:
        driver.find_element("css selector", "#buyFactory").click()
    elif money >= grandma:
        driver.find_element("css selector", "#buyGrandma").click()
    elif money >= cursor:
        driver.find_element("css selector", "#buyCursor").click()


timeout = time.time() + 60*5
check_interval = time.time() + 5


while True:
    cookie.click()
    if time.time() >= check_interval:
        purchase()
        check_interval = time.time() + 5
    if time.time() >= timeout:
        break
