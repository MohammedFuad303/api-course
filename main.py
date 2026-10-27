import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("GITHUB_TOKEN")


def check_token():
    if api_key:
        print(f"Token loaded, length: {len(api_key)}")
    else:
        print("Token not found")


def api_call():
    url =  "https://api.github.com"
    response = requests.get(url)
    data = response.json()
    print(data["emojis_url"])


def api_call2():
    response = requests.get("https://api.github.com/emojis")
    data = response.json()
    #print(data)
    print(data["zombie_woman"])
    #print(data["rocket"])


def search_repos():
    url = "https://api.github.com/search/repositories"
    params = {"q" : "agent",
              "per_page" : 3
              }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        #print(response.url)
        for repo in response.json()["items"]:
            print(repo["full_name"])
    except requests.exceptions.RequestException as error:
        print(f"Sorry, could not fetch your request: {error}")


def broken_call():
    url = "https://api.github.com/this-does-not-exist"
    response = requests.get(url)
    print(response.status_code)


def exception_handling():
    
    try:
        url = "https://api.this-domain-does-not-exist-12345.com"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as error:
        print(f"Sorry, could not fetch your request : {error}.")


def show_headers():
    url = "https://api.github.com"
    headers = {
        "Accept" : "application/vnd.github+json"
    }
    response = requests.get(url, timeout=5, headers=headers)
    #print(response.headers["Content-Type"])
    
    print(response.status_code)

def check_api_limit():
    url = "https://api.github.com/rate_limit"
    response = requests.get(url, timeout=5)
    data = response.json()
    print(data["rate"])


def check_api_limit_with_key():
    url = "https://api.github.com/rate_limit"
    headers = {
        "Authorization" : f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers, timeout=5)
    data = response.json()
    print(data["rate"])


#api_call()

if __name__  == "__main__":
    check_api_limit_with_key()