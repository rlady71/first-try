import requests
res = requests.get("http://google.com")
res.raise_for_status() # 접근 안되면 err 띄움

print("응답코드 :", res.status_code) # 200이면 정상

if res.status_code == requests.codes.ok:
    print("정상")
else:
    print("문제. 코드 : ", res.status_code)


print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)