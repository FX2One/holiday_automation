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

driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.wakacje.pl/wczasy/')

#accept cookies
cookie_clause = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/button[2]'))).click()

#user rating
user_rating = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[5]/div[2]/div/div/div[2]/div/div[1]'))).click()

#user rating above 8.5
ur_above = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[5]/div[2]/div/div/div[2]/div/div[2]/span[7]'))).click()

#first minute
first_minute = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[6]/div[2]/div/div[1]/div/div'))).click()

#find airport tab and click
airport = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[3]/div/div').click()
time.sleep(3)

#select airport
poznan_airport = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/ul/li[9]/label/div').click()
time.sleep(1)
#search offer
poznan_search_offer = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/footer/button').click()
time.sleep(1)

#destination tab
destination_div = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input').click()
time.sleep(1)

#destination input box to select city
destination_input = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input')
time.sleep(1)

#pick greece
greece = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/ul[2]/div[48]/li/label/div').click()

time.sleep(5)
#find offer
find_offer_button = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/footer/button').click()
time.sleep(1)

#select max date
smax = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div').click()

smax_value = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span[10]').click()

time.sleep(1)

#select all-inclusive
all_inc = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[2]/div[2]/div/div[1]/div/div').click()
time.sleep(2)

#price input

price_inp = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[4]/div[2]/div/div[1]/div/div[2]/div[2]/div/input')
price_inp.send_keys('3000')
time.sleep(2)

#star hotel
star_hotel = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[3]/div[2]/div/div[3]/div').click()
time.sleep(2)

#last minute
last_minute = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[6]/div[2]/div/div[3]/div/div'))).click()

#search for final offer
final_offer =WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[11]/div/button'))).click()


