from flask import Blueprint, request, render_template

book_routes = Blueprint("book_routes", __name__)


@book_routes.route("/book")
def book_form():
    print("Book Form...")
    return render_template("book_form.html")

@book_routes.route('/submit_book', methods=['POST'])
def submit_book():
    title = request.form.get('title')
    author = request.form.get('author')
    description = request.form.get('description')
    new_book = {
        'title': title,
        'author': author,
        'description': description
    }
    #books.append(new_book)
    print(new_book)
    return new_book
    
