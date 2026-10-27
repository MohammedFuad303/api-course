import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GITHUB_TOKEN")

def first_project():
    url = "https://api.github.com/search/repositories"
    word = input("Search for: ")
    params = {
        "q" : word,
        "per_page" : 5
    }
    headers = {
        "Authorization" : f"Bearer {api_key}"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        for repo in data["items"]:
            print(repo["full_name"])
    except requests.exceptions.RequestException as err:
        print(f"Sorry could not fetch your request: {err}")


if __name__ == "__main__":
    first_project()

