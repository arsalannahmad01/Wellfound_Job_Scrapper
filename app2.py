import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_data():
    url = "https://wellfound.com/discover/startups?location=bangalore-urban"
    all_urls = []
    try:
        browser = Chrome(headless=True)
        browser.get(url)

        browser.save_screenshot("first_screenshot.png")

        urls = browser.find_elements(By.CSS_SELECTOR, '#main > div.styles_component__VRc0I.styles_white__Nexe6 > div > div > main > div > div:nth-child(3) > div.mb-14 > div > div:nth-child(1) > a').get('href')
        browser.save_screenshot("second_screenshot.png")

        # for url in urls:
        #     link = url.get('href')
        
        print(urls)
    except Exception as e:
        print('Error: ', e)
    finally:
        browser.quit()

fetch_data()

# def fetch_urls():

#     url = "https://wellfound.com/discover/startups?location=bangalore-urban"
#     all_urls = []

#     try:

#         options = webdriver.ChromeOptions()
       
#         options.add_argument('--headless')

#         # driver = webdriver.Chrome(options=options)

#         driver = Chrome(headless=True)

#         driver.get(url)

#         driver.save_screenshot("first_screenshot.png")


#         time.sleep(15)
#         html = driver.page_source

#         driver.save_screenshot("second_screenshot.png")

#         soup = BeautifulSoup(html, 'html.parser')
#         link_units = soup.find('div', {'class':'space-y-4 md:columns-2 lg:columns-3 mt-10'}).find_all('div', {'class':'styles_component__uM9l6 h-[280px] relative overflow-hidden rounded-lg border border-gray-400 hover:border-gray-600 hover:bg-gray-100'})

#         driver.save_screenshot("third_screenshot.png")


#         for link_unit in link_units:
#             time.sleep(15)
#             link = link_unit.find('a').get('href')
#             all_urls.append("https://wellfound.com" + link)


       

#     except Exception as e:
#         print('Error:', e)
#         driver.save_screenshot("error_screenshot.png")
#     finally:
#         time.sleep(15)
#         driver.save_screenshot("final_screenshot.png")
#         driver.quit()

#     return all_urls

# def fetch_company_data(url):

#     try:

#         options = webdriver.ChromeOptions()
     
#         options.add_argument('--headless') 

#         # driver = webdriver.Chrome(options=options)
#         driver = Chrome(headless=True)


#         driver.get(url)

#         time.sleep(15)
#         html = driver.page_source
        
#         driver.save_screenshot("1st_screenshot.png")

#         soup = BeautifulSoup(html, 'html.parser')
#         company_data = soup.find('div', {'class':'styles_content__pKhb0'})
        
#         company_name = company_data.find('h3', {'class':"styles-module_component__3ZI84 styles_companyHeader__OZlL0 text-xl font-medium"}).find('a').getText()
        
#         driver.save_screenshot("2nd_screenshot.png")

#         time.sleep(15)
#         company_about = company_data.find('div', {'class':"styles_description__YMjmO"}).find('div').getText()

#         driver.save_screenshot("3rd_screenshot.png")

#         time.sleep(15)
#         company_size_funding = company_data.find('div', {'class':"styles_component__Wb41n styles_component__qhaPy styles_about__6dvji styles_white__yJuQK"}).find('dl').find_all('dt')
#         time.sleep(3)
#         company_size = company_size_funding[2].getText()
#         time.sleep(3)
#         company_funding = company_size_funding[3].getText()


#         print("Company Name: " + company_name)
#         print("About Company: " + company_about)
#         print("Company Size: " + company_size)
#         print("Company Funding: " + company_funding)

#         # for link_unit in link_units:
#         #     link = link_unit.find('a').get('href')
#         #     all_urls.append("https://wellfound.com/" + link)


       

#     except Exception as e:
#         print('Error:', e)
#         driver.save_screenshot("error_screenshot.png")
#     finally:
#         driver.save_screenshot("final_screenshot.png")
#         driver.quit()


# def main():
#     all_urls = fetch_urls()
#     print(all_urls)
#     for url in all_urls:
#         time.sleep(random.uniform(60,  100))
#         fetch_company_data(url)

# main()