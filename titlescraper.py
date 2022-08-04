from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv = Service('path of chromedriver.exe')
driver = webdriver.Chrome(service=serv)

driver.get("https://www.imdb.com/search/title/?title_type=feature&languages=en")

titles = driver.find_elements(by=By.CSS_SELECTOR, value="h3.lister-item-header a")

movielist = []
for title in titles:
    movielist.append(title.text)

driver.quit()

for item in movielist:
    print(item)
