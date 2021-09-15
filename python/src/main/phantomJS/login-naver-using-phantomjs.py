from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://nid.naver.com/nidlogin.login"

# PhantomJS 드라이버 추출하기 --- (*1)
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# URL 읽어 들이기 --- (*3)
browser.get(url)

# 로그인
element_id = browser.find_element_by_id("id") # 아이디 텍스트 입력 상자
element_id.clear()  #  텍스트 박스 안 클리어 하기
element_id.send_keys("[아이디]")

element_pw = browser.find_element_by_id("pw") # 비밀번호 텍스트 입력 상자
element_pw.clear()  #  텍스트 박스 안 클리어 하기
element_pw.send_keys("[비밀번호]")

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

browser.save_screenshot("Website_C.png")

# 브라우저 종료하기 --- (*5)
browser.quit()
