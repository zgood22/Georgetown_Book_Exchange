from dotenv import load_dotenv
from IPython.display import Image, display 
import os

load_dotenv()

ISBNdb_key = os.getenv("ISBNdb_key")

import requests

def get_book_details(title):
    # Replace 'your_api_key' with your actual ISBNdb API key
    api_key = ISBNdb_key
    url = f'https://api.isbndb.com/books/{title}'

    headers = {
        'Authorization': ISBNdb_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        books = data.get('books', [])
        if books:
            book = books[0]  # Assuming we take the first book in the list

            author = book.get('authors', 'Author not found')
            edition = book.get('edition', 'Edition not available')
            image_url = book.get('image', 'Image not available')
            published_date = book.get('date_published', 'Publish date not available')

            return author, edition, image_url, published_date
        else:
            return "No book found with that title.", None, None, None
    else:
        return "Failed to retrieve data from ISBNdb.", None, None, None

# Accept user input
book_title = input("Enter a book title: ")
author_name,  edition, image_url, published_date = get_book_details(book_title)

print(f"Author Name: {author_name}")
print(f"Edition: {edition}")
display(Image(url=image_url))
print(f"Date Published: {published_date}")

