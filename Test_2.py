import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.rushplace.com/")
addGood=driver.find_element_by_xpath("//li[1]//a[@rel='nofollow']")
addGood.click()
time.sleep(1)
addGood=driver.find_element_by_xpath("//li[2]//a[@rel='nofollow']")
addGood.click()
time.sleep(1)
addGood=driver.find_element_by_xpath("//li[3]//a[@rel='nofollow']")
addGood.click()
time.sleep(1)
basket=driver.find_element_by_xpath("//span[@class='subtotal']")
basket.click()
#driver.get("http://www.rushplace.com/basket/")
count=driver.find_elements_by_xpath("//tr[@class='woocommerce-cart-form__cart-item cart_item']")
if len(count)==3:
    print("В корзине 3 товара")
else:
    print("Ошибка. Количество товаров в корзине"+str(len(count)))
driver.quit()