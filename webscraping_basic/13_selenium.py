from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()
elem.send_keys("슬램덩크 극장판")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements(By.TAG_NAME,"a")
for e in elem:
    e.get_attribute("href")

elem = browser.find_element(By.XPATH, "xpath 입력")

browser.close() # 탭만 닫음
browser.quit() # browser 다 닫음