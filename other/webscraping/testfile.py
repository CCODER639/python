from bs4 import BeautifulSoup
import requests

url = "https://www.propertynews.com/property-for-sale/detached-houses-type/2-beds/page-2/?paddockStables=true"

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# Find all divs with class "c-result__body"
results = doc.find_all("p", class_="o-type o-type--big-contrast")

for div in results:
    print(div.get_text(strip=True))

file = "file.txt"
with open(file, "w") as f:
    for div in results:
        f.write(div.get_text(strip=True))
        f.write("\n\n")