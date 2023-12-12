from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

# Get the ISBNdb API key from environment variables
ISBNdb_key = os.getenv("ISBNdb_key")

def get_book_details(title):
        api_key = ISBNdb_key
        url = f'https://api.isbndb.com/books/{title}'
        headers = {'Authorization': ISBNdb_key}

        # Send a GET request to the ISBNdb API
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            books = data.get('books', [])
            
            if books:
                # Limit the results to top 8 books
                top_books = books[:8]

                # Prepare the list of book details
                book_details = []
                for book in top_books:
                    book_info = {
                        'author': book.get('authors', 'Author not found'),
                        'edition': book.get('edition', 'Edition not available'),
                        'image_url': book.get('image', 'Image not available'),
                        'published_date': book.get('date_published', 'Publish date not available')
                    }
                    book_details.append(book_info)

                return book_details
            else:
                return "No book found with that title."
        else:
            return "Failed to retrieve data from ISBNdb."

if __name__ == '__main__':
     book_search = input('Please enter the name of the book you are searching for: ')
     book_details = get_book_details(book_search)
     print(book_details[1])