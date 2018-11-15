import abuyun
from selenium import webdriver
import time
import myconfig as cfg

#以手机端打开
mobile_emulation = {"deviceName":"iPhone 6"}
abuyun.option.add_experimental_option('mobileEmulation', mobile_emulation)

count = 1

while True:
    try:
        print(count)
        driver = webdriver.Chrome(chrome_options=abuyun.option)
        driver.delete_all_cookies()
        driver.get(cfg.voteurl)
        driver.implicitly_wait(5)
        js = cfg.votejs
        driver.execute_script(js)
        time.sleep(1)
        count =count + 1
    except:
        print("err")
        continue
    finally:
        driver.quit()