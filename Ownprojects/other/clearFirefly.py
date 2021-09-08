from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='./chromedriver 2')
driver.get("https://bishopstopford.fireflycloud.net/set-tasks#ms=All&p=1&ps=All&sb=DueDate&smss=All&so=Descending&sp=Todo&srs=All&ss=Active&tt=All")
time.sleep(60)
while True:
    try:
        tick_box = driver.find_element_by_xpath('//*[@id="task-select-all"]')
        tick_box.click()
        time.sleep(2)
        button = driver.find_element_by_xpath('//*[@id="react-task-listing"]/main/section/div[1]/div[2]/div[1]/div[1]/div[2]/div/button')
        button.click()
        time.sleep(5)
    except:
        time.sleep(10)
