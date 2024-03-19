import random
from selenium import webdriver
import  undetected_chromedriver as uc
from selenium_stealth import stealth

proxies = [
    "183.172.246.197:7890",
    "201.236.248.250:5678",
    "103.86.1.22:4145",
    "190.120.249.149:4145",
    "203.80.190.162:8080",
    "172.67.105.234:80"
]

# proxy = random.choice(proxies)
# options.add_argument("start-maximized")

# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

options = uc.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('--disable-gpu')
driver = uc.Chrome(options=options)
# options.add_argument(f'--proxy-server={proxy}')


# stealth(driver, languages=["en-Us", 'en'],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline= False,)
