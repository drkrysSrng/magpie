from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver, StandardDelayConfig
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from time import sleep
import random

# Option 1
# Create a UserAgent object
user_agent = UserAgent()

# Generate a random User-Agent string
random_user_agent = user_agent.random

# Option 2
# Common User Agents for Various Devices and Browsers with their screen resolutions
user_agents = {
    # Smartphones
    "Smartphone_Chrome": [
        "Mozilla/5.0 (Linux; Android 10; Mobile; rv:100.0) Gecko/100.0 Firefox/100.0",
        "Mozilla/5.0 (Linux; Android 11; Mobile; rv:100.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Mobile Safari/537.36",
    ],
    "Smartphone_Safari": [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    ],

    # PCs
    "PC_Chrome": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    ],
    "PC_Edge": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0 Safari/537.36",
    ],

    # Mac
    "Mac_Safari": [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    ],

    # Tablets
    "Tablet_Chrome": [
        "Mozilla/5.0 (Linux; Android 11; Tablet; rv:100.0) Gecko/100.0 Firefox/100.0",
    ],
    "Tablet_Safari": [
        "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    ],
}

# Common Screen Resolutions for Each Category
smartphone_resolutions = [
    (320, 480), (640, 960), (640, 1136), (750, 1334), (1080, 1920), (828, 1792), (1125, 2436), (1242, 2688),
]

pc_resolutions = [
    (1920, 1080), (1366, 768), (1280, 800), (1440, 900), (1600, 900), (1680, 1050), (1920, 1200), (2560, 1440),
]

mac_resolutions = [
    (2560, 1600), (2880, 1800), (5120, 2880),
]

tablet_resolutions = [
    (768, 1024), (1536, 2048), (1668, 2388),
]

# Randomly select a category (Device + Browser)
category = random.choice(list(user_agents.keys()))
random_user_agent = random.choice(user_agents[category])

# Randomly select a screen resolution based on the category
if "Smartphone" in category:
    random_resolution = random.choice(smartphone_resolutions)
elif "PC" in category:
    random_resolution = random.choice(pc_resolutions)
elif "Mac" in category:
    random_resolution = random.choice(mac_resolutions)
else:
    random_resolution = random.choice(tablet_resolutions)

# Extract width and height
width, height = random_resolution



print(f"We are using {random_user_agent} and resolution {random_resolution}")


proxy_user = ""
proxy_password = ""
proxy_host = ""
proxy_port = ""

proxy = f"socks5h://{proxy_user}:{proxy_password}@{proxy_host}:{proxy_port}"

proxy_host = "127.0.0.1"
proxy_port = "9052"

#proxy = f"socks5h://{proxy_host}:{proxy_port}"

email = "larosi_motomami@gmail.com"
password = "mypass"

sleep(10)

# Create Firefox options
firefox_options = Options()

# Set the custom user agent in Firefox options
firefox_options.set_preference("general.useragent.override", random_user_agent)

#firefox_options.add_argument("-headless")

# Disable extensions
firefox_options.set_preference("extensions.enabled", False)

# Disable the sandbox
firefox_options.set_preference("security.sandbox.content.level", 0)


# Extract width and height
width, height = random_resolution
# Set the initial window size
firefox_options.set_preference("browser.window.width", width)
firefox_options.set_preference("browser.window.height", height)

options = {
    'proxy': {
        'http': proxy,
        'https': proxy,
        'no_proxy': 'localhost,127.0.0.1'
    }
}
# If you want to use a proxy
driver = webdriver.Firefox(options=firefox_options, seleniumwire_options=options)

# Without proxy
#driver = webdriver.Firefox(options=firefox_options)


# Set a delay between requests to simulate human behavior
delay_between_requests = 5  # Adjust this as needed
driver.implicitly_wait(delay_between_requests)


solver = RecaptchaSolver(driver=driver, delay_config=StandardDelayConfig())


driver.get("https://ipinfo.io")

sleep(10)
#driver.get("https://app.hushed.com/login")

driver.get("https://app.hushed.com/signup")


sleep(5)

username_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']")

password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")

username_input.send_keys(email)

sleep(10)

password_input.send_keys(password)

sleep(10)

recaptcha_iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")

solver.click_recaptcha_v2(iframe=recaptcha_iframe)

# Press submit button
sleep(10)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(10)
print("It works!")
sleep(5)