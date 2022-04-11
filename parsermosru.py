import time
from dataclasses import dataclass


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

path_to_chromedriver = 'chromedriver.exe'

@dataclass
class Result:
    index : str
    title: str
    url: str
    values_today: str
    values_week: str
    values_month: str

pages_count=13
spisok=[]

driver = webdriver.Chrome(executable_path = path_to_chromedriver)

for page_number in range(pages_count+1)[1:]:
    driver.get("https://www.mos.ru/dit/function/o-departamente/stats/?page=1"+ str(page_number))

    time.sleep(4)
    elements: list[WebElement]=driver.find_elements(by=By.XPATH,  value="//li[@data-item='item']")


    xpath_index="./div/div[@class='stat_item__index-group']/div[1]"
    xpath_title="./div/div[@class='stat_item__title']/div[contains(@class,'stat_item__title_name')]"
    xpath_url="./div/div[@class='stat_item__title']/a"

    xpath_values_today="./div/div[@class='stat_item__value-group']/div[1]/div[1]"
    xpath_values_week="./div/div[@class='stat_item__value-group']/div[2]/div[1]"
    xpath_values_month="./div/div[@class='stat_item__value-group']/div[3]/div[1]"

    for i in elements:
        index=i.find_element(by=By.XPATH,  value=xpath_index).text
        title = i.find_element(by=By.XPATH, value=xpath_title).text
        url = i.find_element(by=By.XPATH, value=xpath_url).text
        values_today = i.find_element(by=By.XPATH, value=xpath_values_today).text
        values_week = i.find_element(by=By.XPATH, value=xpath_values_week).text
        values_month = i.find_element(by=By.XPATH, value=xpath_values_month).text

        spisok.append(Result(index=index,title=title, url=url, values_today=values_today, values_week=values_week, values_month=values_month))

print(spisok)
file = open('output.txt', 'w')
for element in spisok:
     file.write(element)
     file.write('\n')
file.close()