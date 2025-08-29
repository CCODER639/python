from bs4 import BeautifulSoup
import requests
fileu = "url.txt"
with open(fileu) as f:
    url1 = f.read()
count = 1
print(url1)  # Optional: print the original URL

# Replace 'page-1' with 'page-{}'
url_template = url1.replace("page-1", "page-{}")

print(url_template)
base_url = url_template

file = "file.txt"
file1 = "file1.txt"

# Read seen listings from file.txt
try:
    with open(file, "r") as f:
        content = f.read()
except FileNotFoundError:
    content = ""

# Clear file1.txt before writing new listings
open(file1, "w").close()

with open(file, "a") as f, open(file1, "a") as f1:
    page = 1
    while True:
        print(f"Checking page {page}...")

        url = base_url.format(page)
        result = requests.get(url).text
        doc = BeautifulSoup(result, "html.parser")

        # Find all listing blocks
        listings = doc.select("div.c-result")  # Each property listing

        if not listings:
            print("No more listings found. Stopping.")
            break

        for listing in listings:
            # Price
            price_tag = listing.find("p", class_="o-type o-type--big-contrast")
            price = price_tag.get_text(strip=True) if price_tag else "No price"

            # Address link and text
            name_tag = listing.find("a", class_="o-type--normal o-type c-result__address-link")
            if not name_tag:
                continue
            name = name_tag.get_text(strip=True)
            fLink = "https://www.propertynews.com" + name_tag.get("href")

            # Bed count: find the <svg> with class for bed, then get parent <span> text
            bed_svg = listing.find("svg", class_="c-icon--bed")
            if bed_svg and bed_svg.parent.name == "span":
                bed_text = bed_svg.parent.get_text(strip=True).replace("\n", "")
            else:
                bed_text = "Beds not found"

            if fLink in content:
                print("Not new:", fLink)
            else:
                entry = f"{price}\n{name}\n{bed_text} beds\n{fLink}\n\n"
                f.write(entry)
                f1.write(entry)
                print("NEW:", fLink)
                count += 1

        page += 1
print(count , "new house")