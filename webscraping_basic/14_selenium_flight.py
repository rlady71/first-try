from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

# 날짜 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button/b").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button/b").click()
time.sleep(1)

# 명수 추가
browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6 select_Passenger__36sFM").click()
time.sleep(1)
browser.find_element(By.CLASS_NAME, "searchBox_outer__9n6IB").click()
time.sleep(1)

# 도착지 설정
browser.find_element(By.LINK_TEXT, "도착").click()
time.sleep(1)
browser.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").send_keys("오사카")
time.sleep(1)
browser.find_element(By.CLASS_NAME, "autocomplete_search_item__2WRSw").click()
time.sleep(1)

browser.find_element(By.LINK_TEXT, "항공권 검색").click()

#try:
#    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "~~")))
#finally:
#    browser.quit()