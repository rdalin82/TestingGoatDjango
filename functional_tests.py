from selenium import webdriver
import time

browser = webdriver.Chrome();
browser.get("http://localhost:8000")
time.sleep(5)
assert 'Django' in browser.title

browser.quit()
