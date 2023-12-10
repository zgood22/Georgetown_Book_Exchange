from flask import Blueprint, request, render_template
from app.book_query import get_book_details


book_routes = Blueprint("book_routes", __name__)


# Assuming you have an existing Blueprint named 'book_routes'
# If not, replace 'book_routes' with your Blueprint name or app

@book_routes.route('/new-listing')
def new_listing():
    return render_template('book_form.html')

@book_routes.route('/listing-search', methods=["GET", "POST"])
def listing_search():
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    author_fname = str(request_data.get("authorFirstName"))
    author_lname = str(request_data.get("authorLastName"))
    author_fullname = author_fname + " " + author_lname
    book_title = str(request_data.get("title"))
    book_results = get_book_details(book_title)
    return render_template('listing_search.html', author_fullname=author_fullname, book_results=book_results)