import requests
import pandas as pd

search_query = "ноутбук"

url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1257786&query={search_query}&resultset=catalog&sort=popular&limit=20"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
data = res.json()

products = data["data"]["products"]

result = []
for product in products:
    result.append({
        "Название": product.get("name"),
        "Цена": product.get("priceU", 0) // 100,
        "Бренд": product.get("brand")
    })

df = pd.DataFrame(result)
df.to_excel("wildberries.xlsx", index=False)
print("✅ Файл сохранён")