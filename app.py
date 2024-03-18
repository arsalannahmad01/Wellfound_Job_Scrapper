import time
import random
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def fetch_urls():

    url = "https://wellfound.com/discover/startups?location=bangalore-urban"
    all_urls = []

    try:

        options = webdriver.ChromeOptions()
       
        options.add_argument('--headless')

        driver = Chrome(headless=True)

        driver.get(url)

        driver.save_screenshot("first_screenshot.png")
        time.sleep(5)
        html = driver.page_source

        driver.save_screenshot("second_screenshot.png")

        soup = BeautifulSoup(html, 'html.parser')
        link_units = soup.find('div', {'class':'space-y-4 md:columns-2 lg:columns-3 mt-10'}).find_all('div', {'class':'styles_component__uM9l6 h-[280px] relative overflow-hidden rounded-lg border border-gray-400 hover:border-gray-600 hover:bg-gray-100'})

        driver.save_screenshot("third_screenshot.png")

        count = 0
        for link_unit in link_units:
            if(count == 2):
                break
            time.sleep(5)
            link = link_unit.find('a').get('href')
            all_urls.append("https://wellfound.com" + link)
            count += 1


       

    except Exception as e:
        print('Error:', e)
        driver.save_screenshot("error_screenshot.png")
        driver.quit()
        fetch_urls()
    finally:
        time.sleep(5)
        driver.save_screenshot("final_screenshot.png")
        driver.quit()

    return all_urls

def fetch_company_data(url):

    companyJsonData = {}

    try:

        options = webdriver.ChromeOptions()
     
        options.add_argument('--headless') 

        # driver = webdriver.Chrome(options=options)
        driver = Chrome(headless=True)


        driver.get(url)

        time.sleep(5)
        html = driver.page_source
        
        driver.save_screenshot("1st_screenshot.png")

        soup = BeautifulSoup(html, 'html.parser')
        company_data = soup.find('div', {'class':'styles_content__pKhb0'})
        
        company_name = company_data.find('h3', {'class':"styles-module_component__3ZI84 styles_companyHeader__OZlL0 text-xl font-medium"}).find('a').getText()
        
        driver.save_screenshot("2nd_screenshot.png")

        time.sleep(5)
        company_about = company_data.find('div', {'class':"styles_description__YMjmO"}).find('div').getText()

        driver.save_screenshot("3rd_screenshot.png")

        time.sleep(5)
        company_size_funding = company_data.find('div', {'class':"styles_component__Wb41n styles_component__qhaPy styles_about__6dvji styles_white__yJuQK"}).find('dl').find_all('dt')
        time.sleep(3)
        company_locations = company_size_funding[1].find_all('a', {'class':'styles_component__UCLp3 styles_defaultLink__eZMqw !text-dark-aaa underline'}).getText()
        time.sleep(3)
        company_size = company_size_funding[2].getText()
        time.sleep(3)
        company_funding = company_size_funding[3].getText()
        time.sleep(3)
        markets = company_data.find_all('a', {'class':"styles_component__UCLp3 styles_defaultLink__eZMqw mb-1 mr-2 last:mr-0"})

        company_markets = []
        for market in markets:
            company_markets.append(market.find('span').getText())


        print("Company Name: " + company_name)
        print("About Company: " + company_about)
        print("Company Size: " + company_size)
        print("Company Funding: " + company_funding)

        company = {
            "name":company_name,
            "About":company_about,
            "size":company_size,
            "funding":company_funding,
            "markets": company_markets,
            "locations":company_locations
        }

        companyJsonData = json.dumps(company, indent=4)
    
       

    except Exception as e:
        print('Error:', e)
        driver.save_screenshot("error_screenshot.png")
        driver.quit()
        fetch_company_data(url)
    finally:
        driver.save_screenshot("final_screenshot.png")
        driver.quit()

    return companyJsonData


def main():
    all_urls = fetch_urls()
    print(all_urls)
    for url in all_urls:
        time.sleep(random.uniform(60,  100))
        print(fetch_company_data(url))

main()