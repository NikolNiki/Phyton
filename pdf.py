import requests
import json

# 1. Завантаження PDF

pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"

response = requests.get(pdf_url)

if response.status_code == 200:
    with open("progit.pdf", "wb") as file:
        file.write(response.content)

    print("PDF файл успішно збережено !")
else:
    print("Помилка завантаження PDF")

# 2. Збереження JSON

json_url = "http://api.open-notify.org/astros.json"
response = requests.get(json_url)

if response.status_code == 200:
    data = response.json()

    with open("astros.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("JSON файл успішно збережено!")
else:
    print("Помилка отримання JSON")