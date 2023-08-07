import requests 
import boto3
import time

base_url = "https://website.com/"
pages = {"portfolio", "contact", "jondoe", "london"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
}


# response = requests.get(base_url, verify=False, headers=headers)
# code = response.status_code

while True:
    for page in pages:
        response = requests.get(f'{base_url}{page}', verify=False, headers=headers)
        code = response.status_code
        if code == 200:
            print(f"{base_url}{page} is healthy")
        else:
            print(f"{base_url}{page} is not responding properly, login and remediate error.")
    time.sleep(120)
