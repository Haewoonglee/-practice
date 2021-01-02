import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")

    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = Beautifulsoup(result.text, "html.parser")
        results = soup.find_all("div".{"class":"-job"})
        for result in results:
          print(result["data-jobid"])


def get_jobs():
    last_page = get_last_page()
    jobs = extract_job(last_page)
    return jobs