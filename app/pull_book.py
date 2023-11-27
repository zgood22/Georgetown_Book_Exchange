from dotenv import load_dotenv
import os

load_dotenv()

ISBNdb_key = os.getenv("ISBNdb_key")

import requests

def get_book_author(title):
    # Replace 'your_api_key' with your actual ISBNdb API key
    api_key = ISBNdb_key
    url = f'https://api.isbndb.com/books/{title}'

    headers = {
        'Authorization': api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        books = data.get('books', [])
        if books:
            # Assuming we take the first book in the list
            return books[0].get('authors', 'Author not found')
        else:
            return "No book found with that title."
    else:
        return "Failed to retrieve data from ISBNdb."

# Accept user input
book_title = input("Enter a book title: ")
author_name = get_book_author(book_title)
print(f"Author Name: {author_name}")
