import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# Creating Instance
option = Options()
# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

# driver_installation
s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(30)

# open_browser
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
time.sleep(2)

# round_trip
round_trip = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/label[2]/div[1]/span")
round_trip.click()
time.sleep(2)

# departure
departure = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
departure.click()
departure.send_keys('Goa')
time.sleep(2)
# d_cities_GOA
cities_departure = driver.find_elements(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div/div/div[2]/ul/li/p")
for city_1 in cities_departure:
    if 'Goa, IN - Dabolim Airport (GOI)' in city_1.text:
        city_1.click()
        break
time.sleep(2)
# destination
destination = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div[5]/div/div/div[1]/input")
destination.click()
destination.send_keys('Ban')
time.sleep(2)
driver.implicitly_wait(30)
# d_cities_BAN
cities_destination = driver.find_elements(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div[5]/div/div/div[2]/ul/li/p")
for city_2 in cities_destination:
    if 'Bangalore, IN - Kempegowda International Airport (BLR)' in city_2.text:
        city_2.click()
        break
time.sleep(2)

#date selection
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[3]/div[3]/div/div/div/div/button[1]").click()

all_dates=driver.find_elements(By.XPATH,"//*[@id='root']/div/div/div[1]/div/div[2]/div/div[3]/div[3]/div/div/div/div/div/ul/div[2]/div/div[2]/div[1]/div[3]/div/div")
for dates in all_dates:
    if '11' in dates.text:
        dates.click()
        time.sleep(3)
        for dates1 in all_dates:
            if '16' in dates1.text:
                dates1.click()
                time.sleep(3)
                break
        break






