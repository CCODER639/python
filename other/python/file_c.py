file = "url.txt"
with open(file) as f:
    url = f.read()

print(url)  # Optional: print the original URL

# Replace 'page-1' with 'page-{}'
url_template = url.replace("page-1", "page-{}")

print(url_template)