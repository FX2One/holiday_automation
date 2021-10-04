from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")


PATH = 'C:\Program Files (x86)\chromedriver.exe'
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.wakacje.pl/wczasy/')

#accept cookies
cookie_clause = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]"))).click()

#find airport tab and click
airport = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.us6ked-5.hRtwjI > section > div > div > div > div:nth-child(3) > div > div').click()
time.sleep(1)

#select airport
poznan_airport = driver.find_element_by_css_selector('body > div.pvbrnm-2.dWhXgX > div.pvbrnm-3.eARhAG > div > div.pvbrnm-10.fsPcKq > div > div.sc-6yp7mv-3.glPYjl > div > div:nth-child(1) > div > div.sc-1eezab2-4.kUiomX > div > div:nth-child(2) > ul > li:nth-child(9) > label > div').click()
time.sleep(1)
#search offer
poznan_search_offer = driver.find_element_by_css_selector('body > div.pvbrnm-2.dWhXgX > div.pvbrnm-3.eARhAG > div > footer > button').click()
time.sleep(1)

#destination tab
destination_div = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input').click()
time.sleep(1)

#destination input box to select city
destination_input = driver.find_element_by_css_selector('body > div.pvbrnm-2.dWhXgX > div.pvbrnm-3.eARhAG > div > div.pvbrnm-10.fsPcKq > div > div.jzqfk3-8.qGDMI > div > div > input')
time.sleep(1)

#pick greece
greece = driver.find_element_by_css_selector('body > div.pvbrnm-2.dWhXgX > div.pvbrnm-3.eARhAG > div > div.pvbrnm-10.fsPcKq > div > div.jzqfk3-3.kHonhY > div > div:nth-child(1) > div > div.sc-1eezab2-4.kUiomX > ul:nth-child(1) > div:nth-child(4) > li > label > div').click()

time.sleep(1)
#find offer
find_offer_button = driver.find_element_by_css_selector('body > div.pvbrnm-2.dWhXgX > div.pvbrnm-3.eARhAG > div > footer > button').click()

time.sleep(1)
'''#filter tab and click
filter_button = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.sc-1uud2qw-0.gbzKDU > div.sc-1qhb28-0.ciDFDc > div > button').click()
time.sleep(1)'''

#select max date
smax = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.us6ked-0.dILvMr > aside > div > div:nth-child(2) > div.sc-106s0lo-8.Papwz > div > div:nth-child(2) > div.sc-1u36cim-0.kyonzr > div').click()
smax_value = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.us6ked-0.dILvMr > aside > div > div:nth-child(2) > div.sc-106s0lo-8.Papwz > div > div:nth-child(2) > div.sc-1u36cim-0.kyonzr > div > div.sc-1u36cim-8.jfqeUf > span:nth-child(10)').click()
time.sleep(1)



#select all-inclusive
all_inc = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.us6ked-0.dILvMr > aside > div > div:nth-child(3) > div.sc-106s0lo-8.Papwz > div > div:nth-child(1) > div > div').click()
time.sleep(0.5)

#price input
price_inp = driver.find_element_by_css_selector('#__next > div > div.sc-1lbbeas-0.hTDHIm > main > div > div.us6ked-0.dILvMr > aside > div > div:nth-child(5) > div.sc-106s0lo-8.Papwz > div > div.sc-12w6ps2-0.kMMrnS > div > div:nth-child(2) > div.dc9rez-0.eddCmn > div > input')
price_inp.send_keys('3000')
time.sleep(0.5)

#star hotel
#user review
#last minute/first minute/bonus 