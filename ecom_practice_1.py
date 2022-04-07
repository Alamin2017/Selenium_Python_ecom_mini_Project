import time

from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver_installation
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()
time.sleep(1)


#for laptops
laptops=driver.find_element(By.XPATH,"//*[text()='Laptops & Notebooks']")
action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(1)
laptops_2=driver.find_element(By.XPATH,"//*[text()='Show All Laptops & Notebooks']")
laptops_2.click()
time.sleep(1)
#for HP
HP=driver.find_element(By.XPATH,"//*[text()='HP LP3065']")
HP.click()
time.sleep(1)

#scroll
add_to_cart_button2=driver.find_element(By.XPATH,"//button[@id='button-cart']")
add_to_cart_button2.location_once_scrolled_into_view
time.sleep(1)

#calender
calender=driver.find_element(By.XPATH,'//i[@class="fa fa-calendar"]')
calender.click()
time.sleep(1)


#date selected for add cart
calender_date=driver.find_element(By.XPATH,"//td[contains(text(),'31')]")
calender_date.click()
time.sleep(1)

add_to_cart_button2.click()
time.sleep(1)
#cart_total
cart_total=driver.find_element(By.XPATH,"//span[@id='cart-total']")
cart_total.click()
time.sleep(1)

checkout=driver.find_element(By.XPATH,"//*[@id='cart']/ul/li[2]/div/p/a[2]")
checkout.click()


#guest_account
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//input[@value='guest']").click()
#clickcontinue
guest_continue=driver.find_element(By.XPATH,"//input[@id='button-account']")
guest_continue.click()
time.sleep(2)

#billing
#driver.implicitly_wait(30)
#firstname
firstname=driver.find_element(By.ID,"input-payment-firstname")
firstname.click()
firstname.send_keys("test_first_name")
time.sleep(1)
#lastname
lastname=driver.find_element(By.ID,"input-payment-lastname")
lastname.click()
lastname.send_keys("test_last_name")
time.sleep(1)
#email
email=driver.find_element(By.ID,"input-payment-email")
email.click()
email.send_keys("test@test.com")
time.sleep(1)
#telephone
telephone=driver.find_element(By.ID,"input-payment-telephone")
telephone.click()
telephone.send_keys("012345678")
time.sleep(1)

#address1
address1=driver.find_element(By.ID,"input-payment-address-1")
address1.click()
address1.send_keys("teststreet 187")
time.sleep(1)
#city
city=driver.find_element(By.ID,"input-payment-city")
city.click()
city.send_keys("frankfurt")
time.sleep(1)
#postcode
postcode=driver.find_element(By.ID,"input-payment-postcode")
postcode.click()
postcode.send_keys("112233")
time.sleep(1)

#country
country=driver.find_element(By.ID,"input-payment-country")
dropdown=Select(country)
dropdown.select_by_index(87)
time.sleep(1)
#region
region=driver.find_element(By.ID,"input-payment-zone")
dropdown1=Select(region)
dropdown1.select_by_visible_text('Hessen')
time.sleep(1)
#continue_button
continue_2=driver.find_element(By.XPATH,"//input[@id='button-guest']")
continue_2.click()
#continue too
continue_3=driver.find_element(By.XPATH,"//input[@id='button-shipping-method']")
continue_3.click()
#payment method and terms and conditions
terms=driver.find_element(By.XPATH,"//input[@name='agree']")
terms.click()
time.sleep(1)
continue_4=driver.find_element(By.XPATH,"//input[@id='button-payment-method']")
continue_4.click()
time.sleep(1)
#confirm order page
final_price=driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]")
print("The final price of the product:"+final_price.text)

confirmation=driver.find_element(By.XPATH,"//input[@id='button-confirm']")
confirmation.click()
time.sleep(2)
#success
success_text=driver.find_element(By.XPATH,"//*[@id='content']/h1")
print(success_text.text)

