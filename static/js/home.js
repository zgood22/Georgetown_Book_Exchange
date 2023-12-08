// Example search function (you'll need to adjust it to your backend search logic)
function searchBooks() {
    var input, filter, cards, cardContainer, title, i;
    input = document.getElementById("bookSearch");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("book-list");
    cards = cardContainer.getElementsByClassName("card");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h5.card-title");
        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

// Add the searchBooks function to the search input field
document.getElementById('bookSearch').addEventListener('keyup', searchBooks);
