import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://example.com/products'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Find all product containers
products = soup.find_all('div', class_='product-item')

# Loop through each product and extract the details
for product in products:
    # Extract the product name
    name = product.find('h2', class_='product-title').text.strip()

    # Extract the product price
    price = product.find('span', class_='product-price').text.strip()

    print(f"Product Name: {name}, Price: {price}")
