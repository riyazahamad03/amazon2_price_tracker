from selenium import webdriver
import requests
from datetime import datetime
import time

ASIN=input("Please Enter Asin of product : ")
ASIN2=input("please Enter Asin of 2nd product :")
Desired_Price=int(input("please enter the desired price ,Which Should Be In The Format Of Less Than < :"))
Desired_Price_f=int(input("please enter the desired price for ASIN2  ,Which Should Be In The Format Of Less Than < :"))
url='https://www.amazon.in/dp/'+ASIN
url_1='https://www.amazon.in/gp/offer-listing/'+ASIN
url_f='https://www.amazon.in/dp/'+ASIN2
url_f1='https://www.amazon.in/gp/offer-listing/'+ASIN2

webdriver_path =r"  "#please enter your webdriver path here
options = webdriver.ChromeOptions()
#options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(webdriver_path,options=options)

def check_price():
    try:
        driver.get(url)
        name = driver.find_element_by_id("productTitle").text
        price=driver.find_element_by_id("priceblock_ourprice").text
        converted_price=float(price.replace("₹","").replace(",","").replace(" ",""))
        if(converted_price < Desired_Price ):
            send_message("\n" "\n"+name+"\n" "\n"+price+ "\n" "\n"+ url)
            print(name)
            print(converted_price)

    except:
        print("*Price Unavaivable Or Not At You Desired Limit " )

    time.sleep(5)
        
    try:
        driver.get(url_1)
        name_1=driver.find_element_by_css_selector("#olpProductDetails > h1").text
        price_1=driver.find_element_by_css_selector("#olpOfferList > div > div > div:nth-child(3) > div.a-column.a-span2.olpPriceColumn > span > span").text
        converted_price_1 = float(price_1.replace(" ","").replace(",",""))
        if (converted_price_1 < Desired_Price):
            send_message("\n" "\n"+name_1+"\n" "\n"+price_1+ "\n" "\n"+ url_1)
            print(name_1)
            print(converted_price_1)
    except:
        print("*Price Unavaivable Or Not At You Desired Limit")
     
    time.sleep(5)
    
    try:
        driver.get(url_f)
        name_f = driver.find_element_by_id("productTitle").text
        price_f=driver.find_element_by_id("priceblock_ourprice").text
        converted_price_f=float(price_f.replace("₹","").replace(",","").replace(" ",""))
        if(converted_price_f < Desired_Price_f ):
            send_message("\n" "\n"+name_f+"\n" "\n"+price_f+ "\n" "\n"+ url_f)
            print(name_f)
            print(converted_price_f)
    except:
        print("*Price Unavaivable Or Not At You Desired Limit")

    time.sleep(5)
        
        
    
    try:
        driver.get(url_f1)
        name_1f=driver.find_element_by_css_selector("#olpProductDetails > h1").text
        price_1f=driver.find_element_by_css_selector("#olpOfferList > div > div > div:nth-child(3) > div.a-column.a-span2.olpPriceColumn > span > span").text
        converted_price_1f = float(price_1f.replace(" ","").replace(",",""))
        if (converted_price_1f < Desired_Price_f):
            send_message("\n" "\n"+name_1f+"\n" "\n"+price_1f+ "\n" "\n"+ url_f1)
            print(name_1f)
            print(converted_price_1f)
    except:
        print("*Price Unavaivable Or Not At You Desired Limit")

    time.sleep(5)
    
        
    

def send_message(bot_message):
    
    bot_token = '  ' #please enter your bot token inside the quotes
    bot_chatID = '  ' #please enter you chat id inside the quotes
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text='+bot_message
    response = requests.get(send_text)
    return response.json()

while(True):
    check_price()
    
