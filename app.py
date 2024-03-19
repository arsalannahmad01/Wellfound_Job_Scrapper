import time
import random
import json
from selenium import webdriver
import  undetected_chromedriver as uc
from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
from driver import driver


def fetch_company(url):
    all_urls = []

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') 
        options.add_argument('--disable-gpu')
        driver = uc.Chrome(options=options)
        driver.get(url)
        driver.save_screenshot("first_screenshot.png")
        
        time.sleep(5)
        html = driver.page_source

        driver.save_screenshot("second_screenshot.png")

        soup = BeautifulSoup(html, 'html.parser')
        link_units = soup.find('div', {'class':'space-y-4 md:columns-2 lg:columns-3 mt-10'}).find_all('div', {'class':'styles_component__uM9l6 h-[280px] relative overflow-hidden rounded-lg border border-gray-400 hover:border-gray-600 hover:bg-gray-100'})

        driver.save_screenshot("third_screenshot.png")

        if(not len(link_units)):
            fetch_company()

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
        time.sleep(2)
        driver.quit()
        time.sleep(2)
        fetch_company()
    finally:
        time.sleep(2)
        driver.save_screenshot("final_screenshot.png")
        driver.quit()

    return all_urls




def fetch_company_data(url):

    try:

        options = webdriver.ChromeOptions()
        options.add_argument('--headless') 
        options.add_argument('--disable-gpu')
        driver = uc.Chrome(options=options)
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
        locations = company_size_funding[1].find_all('a', {'class':'styles_component__UCLp3 styles_defaultLink__eZMqw !text-dark-aaa underline'})
        company_locations = []

        for location in locations:
            company_locations.append(location.getText())


        time.sleep(3)
        company_size = company_size_funding[2].getText()
        time.sleep(3)
        company_funding = company_size_funding[3].getText()
        time.sleep(3)
        markets = company_data.find_all('a', {'class':"styles_component__UCLp3 styles_defaultLink__eZMqw mb-1 mr-2 last:mr-0"})

        company_markets = []
        for market in markets:
            company_markets.append(market.find('span').getText())

        types = company_data.find_all('span', {'class':'mb-1 styles-module_component__2E93_ inline-flex flex-row items-center mr-2 last:mr-0 rounded-full align-middle bg-gray-200 text-gray-700 gap-2 text-xs px-3 py-1'})
        company_types = []
        for type in types:
            company_types.append(type.getText())

        jobs_count = soup.find('div', {'class':'flex justify-center gap-1'}).find('span').getText()

        jobs_links = soup.find_all('a', {'class':'styles_component__UCLp3 styles_defaultLink__eZMqw styles_anchor__aTiEC'})
        company_jobs = []
        for job_link in jobs_links:
            company_jobs.append("https://wellfound.com"  + job_link.get('href'))


        print("Company Name: " + company_name)
        print("About Company: " + company_about)
        print("Company Size: " + company_size)
        print("Company Funding: " + company_funding)
        print("Company locations: ", company_locations)
        print("Company markets: ", company_markets)
        print("Company Types: ", company_types)
        print('Number of jobs: ' + jobs_count)
        print('Jobs: ', company_jobs)

        # company = {
        #     "Name":company_name,
        #     "About":company_about,
        #     "Company_size":company_size,
        #     "Funding":company_funding,
        #     "Markets": company_markets,
        #     "Locations":company_locations,
        #     "Company_type" : company_types,
        #     "Jobs_count" : jobs_count,
        #     "Jobs":company_jobs
        # }

        # companyJsonData = json.dumps(company, indent=4)

    except Exception as e:
        print('Error:', e)
        driver.save_screenshot("error_screenshot.png")
        time.sleep(2)
        driver.quit()
        time.sleep(2)
        fetch_company_data(url)
    finally:
        driver.save_screenshot("final_screenshot.png")
        driver.quit()

    # return companyJsonData




def main():

    url = "https://wellfound.com/discover/startups?location=bangalore-urban"
    all_urls = fetch_company(url)
    
    # print(json.loads(all_urls))
    for url in all_urls:
        time.sleep(random.uniform(60,  100))
        fetch_company_data(url)

main()