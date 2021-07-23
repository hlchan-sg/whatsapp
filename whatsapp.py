"""this script sends out messages to your whatsapp contact automatically through chrome webdriver"""

### import modules
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

### start whatsapp web on chrome
chrome_path = 'C:\Python39\Scripts\chromedriver.exe'
chrome_history = r'C:\Users\Stephen\AppData\Local\Google\Chrome\User Data\Default'
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir={chrome_history}')
driver = webdriver.Chrome(executable_path=chrome_path, options=options)
driver.get('https://web.whatsapp.com')
driver.implicitly_wait(20)

### variables on person/ group and messages
"""Replace target with the name of your friend or the name of a group"""
target = "Hello"   # person or group to send message to

"""Replace the below string with your own message"""
s1 = "i give you a like"
s2 = "credit you S$0.01"
s3 = "x 10 times, ok?"

### code to find elements in chrome
"""code to find target in http"""
x_arg = '//span[contains(@title,"'+target+'")]'
group_title = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

"""code to find input box in http"""
inp_css = 'div[data-tab="6"]'
input_box = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, inp_css)))
input_box.click()

### send out the message in the above variables
input_box.send_keys(f'{s1}', Keys.ENTER)
time.sleep(10)
input_box.send_keys(f'{s2}', Keys.ENTER)
time.sleep(10)
for i in range(3):
    input_box.send_keys(f'{s3}', Keys.ENTER)
    time.sleep(5)