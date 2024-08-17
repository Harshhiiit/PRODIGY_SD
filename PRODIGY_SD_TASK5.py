import requests
from bs4 import BeautifulSoup
import pandas as pd

# The rest of your code...


# Define the URL of the website to scrape
url = 'http://books.toscrape.com/'

# Send a request to fetch the HTML content
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to fetch webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Lists to store the data
book_titles = []
book_prices = []
book_ratings = []

# Find all the books on the page
books = soup.find_all('article', class_='product_pod')

for book in books:
    # Extract the title of the book
    title = book.h3.a['title']
    book_titles.append(title)

    # Extract the price of the book
    price = book.find('p', class_='price_color').text
    book_prices.append(price)

    # Extract the rating of the book
    rating = book.p['class'][1]  # The rating is stored in a class name like 'star-rating Three'
    book_ratings.append(rating)

# Create a DataFrame from the scraped data
data = {
    'Title': book_titles,
    'Price': book_prices,
    'Rating': book_ratings
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('scraped_books.csv', index=False)

print("Data successfully saved to 'scraped_books.csv'")
