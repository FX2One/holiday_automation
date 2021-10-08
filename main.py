from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.wakacje.pl/wczasy/')

timer = 20

#accept cookies
cookie_clause = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/button[2]'))).click()


#user rating
user_rating = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[10]/div[2]/div/div[3]/div/div'))).click()


#find airport tab and click
airport = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[3]/div/div'))).click()

#select airport
poznan_airport = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/ul/li[9]/label/div'))).click()

#search offer
poznan_search_offer = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[1]/div/footer/button'))).click()


#destination tab
destination_div = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input'))).click()


#destination input box to select city
destination_input = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input')


#pick greece
greece = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/ul[2]/div[48]/li/label/div'))).click()


#find offer
find_offer_button = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[1]/div/footer/button'))).click()


#select all-inclusive
all_inc = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[1]/div[2]/div/div[1]/div/div'))).click()


#price input
price_inp = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div/input')
price_inp.send_keys('3000')


#star hotel
star_hotel = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[2]/div[2]/div/div[3]/div/div'))).click()


#search for final offer
final_offer =WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/aside/div/div[11]/div/button'))).click()


