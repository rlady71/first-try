import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split('\t')
writer.writerow(title)

for page in range(1,5):

    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr",attrs={"onmouseover":"mouseOver(this)"})

    for row in data_rows:
        rank = row.find("td",attrs={"class":"no"}).get_text()
        name = row.find("a").get_text()
        columns_number = row.find_all("td", attrs={"class":"number"})
        data_number = [column.get_text().strip() for column in columns_number]
        #print("종목명 : ",name, " ", data)
        data = [rank] + [name] + data_number
        writer.writerow(data)




    #stocks = soup.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
    
    #for stock in stocks:
    #    name = stock.find("a").get_text()
    #    print("종목명 : ", name)