#导入模块
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
sparker  = win32com.client.Dispatch("SAPI.SpVoice")

#打开浏览器
browser = webdriver.chrome()
#进入某个页面
browser.get("https://www.jd.com/")
time.sleep(3)
#扫描登录
browser.find_element(By.LINK_TEXT,"你好，请登录").click()
print(f"请扫码")
time.sleep(8)
#打开购物车
browser.get("https://cart.jd.com/cart_index")
time.sleep(5)
#全选购物车
while True:
    if browser.find_element(By.CLASS_NAME,'jdcheckbox'):
        browser.find_element(By.CLASS_NAME,'jdcheckbox').click()
        break
    
while True:
    #获取电脑时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%F')
    #对比时间，时间到的话就点击结算
    print(now)
    #判断是不是秒杀时间
    if now >= '2023-03-03 16:40:10':
        #点击结算
        while 1==1:
            try:
                if browser.find_element(By.LINK_TEXT,"你好，请结算"):
                    print("here")
                    browser.find_element(By.LINK_TEXT,"你好，请结算").click()
                    print(f"主人，结算提交成功，请及时支付")
                    break
            except:
                pass
        #点击提交订单
        while True:
            try:
                if browser.find_element(By.LINK_TEXT,"提交订单"):
                    browser.find_element(By.LINK_TEXT,"提交订单").click
                    print(f"抢购成功，请尽快支付")
            except:
                print(f"主人，我已帮你抢到商品，快来支付吧")
                break
        time.sleep(0.01)
                