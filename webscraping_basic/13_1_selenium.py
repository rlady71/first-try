import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

# 3. ID, PW 입력
browser.find_element(By.ID,"id").send_keys("rlady")
browser.find_element(By.ID,"pw").send_keys("!qwe1212")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(2)

# 5. id를 새로 입력
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("rlady71")
browser.find_element(By.ID,"pw").send_keys("!qwe1212")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit()