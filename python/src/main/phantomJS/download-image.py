from selenium import webdriver

url = "https://www.naver.com"

# PhantomJS 드라이버 추출하기 --- (*1)
browser = webdriver.PhantomJS()

# 3초 대기하기 --- (*2)
browser.implicitly_wait(3)

# URL 읽어 들이기 --- (*3)
browser.get(url)

# 화면을 캡처해서 저장하기 --- (*4)
# 아래의 *4번 부분이 실질적인 구동의 역역입니다.
browser.save_screenshot("Website.png")

# 브라우저 종료하기 --- (*5)
browser.quit()
