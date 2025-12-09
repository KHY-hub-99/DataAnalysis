from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://comic.naver.com/webtoon/detail?titleId=776601&no=178&week=fri"

# 베스트 댓글
def best(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    xpath = "/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li"
    best_comment_elements = driver.find_elements(By.XPATH, xpath)
    time.sleep(3)

    best_li = []
    for li in best_comment_elements:
        try:
            comment_p = li.find_element(By.XPATH, "./div[1]/div[2]/div/p")
            comment_text = comment_p.text.strip()
            best_li.append(comment_text)
        except Exception as e:
            continue
    
    return best_li


# 전체 댓글
def all(url):
    d = webdriver.Chrome()
    d.get(url)
    time.sleep(3)
    d.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/div[4]/button[2]").click()
    time.sleep(3)
    x = "/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li"
    cm = d.find_elements(By.XPATH, x)
    time.sleep(3)

    all_comment = []
    for li in cm:
        try:
            comment_p = li.find_element(By.XPATH, "./div[1]/div[2]/div/p")
            comment_text = comment_p.text.strip()
            all_comment.append(comment_text)
        except Exception as e:
            continue
    
    return all_comment


ac = best(url)
print(ac)