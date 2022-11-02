import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

for year in range(2018,2023):

    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(year)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("div", attrs={"class":"thumb"})

    for idx, k in enumerate(images):
        image_url = k.find("img")["src"]
        #print(image["src"])
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break