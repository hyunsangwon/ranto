from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import math

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # 브라우저 숨김 모드 실행 (필요 시 제거)
driver = webdriver.Chrome(options=options)

# category0

# 네이버 블로그 URL 설정
base_url = "https://blog.naver.com/ranto28"

def extract_page_data(driver):
    data = []
    try:
        posts = driver.find_elements(By.CSS_SELECTOR, "table.blog2_list.blog2_categorylist span.ell2.pcol2 a")
        for post in posts:
            title = post.text.strip()
            link = post.get_attribute("href")
            data.append({"title": title, "link": link})
    except Exception as e:
        print(f"Error extracting page data: {e}")
    return data

def click_pages(driver):
    all_data = []
    # 초기 URL로 이동
    driver.get(base_url)
    # iframe으로 전환
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mainFrame")))
     # 'category0' 아이디를 가진 요소 클릭
    category_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "category0"))
    )
    category_element.click()
    time.sleep(2)  # 페이지 로딩 대기

    total = 1483
    pages = math.ceil(total / 15)
    print('pages : ', pages)
    for page_num in range(1, pages):
        try:
            # 페이지 버튼 클릭 (XPath 사용)
            if(page_num == 1):
                page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//strong[contains(@class, '_param({page_num})')]")))
            else:
                page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, '_param({page_num})')]")))
            page_button.click()
            time.sleep(2)  # 페이지 로딩 대기
            
            # 현재 페이지 데이터 추출
            page_data = extract_page_data(driver)
            all_data.extend(page_data)
            print(f"Page {page_num} 크롤링 완료")

        except Exception as e:
            print(f"Error navigating to page {page_num}: {e}")
    
    return all_data

# 크롤링 실행
data = click_pages(driver)
# 결과를 CSV 파일로 저장
df = pd.DataFrame(data)
df.to_csv("ranto.csv", index=False, encoding="utf-8-sig")
print("크롤링 완료! 결과가 'ranto.csv'에 저장되었습니다.")
# 브라우저 종료
driver.quit()
