import requests
import pydnsbl

# Specify the URL you want to request
url_list = ["https://ipinfo.io/ip", "http://ipconfig.io/ip", "http://ifconfig.me", "http://icanhazip.com",
            "http://ipecho.net/plain", "http://ip-api.com/line/?fields=query"]

# Proxy with password


proxy_user = ""
proxy_password = ""
proxy_host = ""
proxy_port = ""

proxy = f"socks5h://{proxy_user}:{proxy_password}@{proxy_host}:{proxy_port}"

# Proxy without Password (if you use nyu proxy)

# proxy_host = "127.0.0.1"
# proxy_port = "9052"

# proxy = f"socks5h://{proxy_host}:{proxy_port}"

# Define the proxy settings
proxy = {
    "http": proxy,  # For HTTP
    "https": proxy,  # For HTTPS
}

for url in url_list:
    # Make an HTTP GET request using the proxy
    response = requests.get(url, proxies=proxy)
    # response = requests.get(url)

    # Check if the request was successful (status code 200 indicates success)
    if response.status_code == 200:

        # Print the content of the response
        ip_checker = pydnsbl.DNSBLIpChecker()

        ip_to_check = response.text

        ip_to_check = ip_to_check.replace("\n", "")

        print("The IP to ask is", ip_to_check)
        response = ip_checker.check(ip_to_check)

        print(f"Is it banned? {response}")

    else:
        print(f"Request failed with status code: {response.status_code}")
