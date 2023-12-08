from flask import Blueprint, request, render_template


book_routes = Blueprint("book_routes", __name__)


# Assuming you have an existing Blueprint named 'book_routes'
# If not, replace 'book_routes' with your Blueprint name or app

@book_routes.route('/new-listing')
def new_listing():
    return render_template('book_form.html')

@book_routes.route('/listing-search')
def listing_search():
    return render_template('listing_search.html')