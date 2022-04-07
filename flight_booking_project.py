import time



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver_installation
s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
#open_browser
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
time.sleep(2)
#round_trip
round_trip=driver.find_element(By.XPATH,"//label[2]//div[1]//span[1]")
round_trip.click()
time.sleep(2)

departure=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div/div/div[1]/input")
departure.click()
departure.send_keys("fra")
time.sleep(2)







