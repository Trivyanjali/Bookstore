
from flask import Flask, render_template, redirect, url_for,session,request,flash
from flask_session import Session
from difflib import get_close_matches
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
books = [
    {'id': 1, 'title': 'Atomic Habits', 'author': 'James Clear', 'price': 450, 'stock': 12, 'image_url': 'https://m.media-amazon.com/images/I/91bYsX41DVL._AC_UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 2, 'title': 'The Psychology of Money', 'author': 'Morgan Housel', 'price': 399, 'stock': 8, 'image_url': 'https://m.media-amazon.com/images/I/71g2ednj0JL._AC_UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 3, 'title': 'Ikigai', 'author': 'Héctor García & Francesc Miralles', 'price': 299, 'stock': 15, 'image_url': 'https://m.media-amazon.com/images/I/81l3rZK4lnL.jpg',"preorder":True},
    {'id': 4, 'title': 'Rich Dad Poor Dad', 'author': 'Robert T. Kiyosaki', 'price': 350, 'stock': 5, 'image_url': 'https://m.media-amazon.com/images/I/81bsw6fnUiL.jpg',"preorder":True},
    {'id': 5, 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'price': 499, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/713jIoMO3UL.jpg',"preorder":True},
    {'id': 6, 'title': 'Educated', 'author': 'Tara Westover', 'price': 399, 'stock': 7, 'image_url': 'https://m.media-amazon.com/images/I/81WojUxbbFL.jpg',"preorder":True},
    {'id': 7, 'title': 'Becoming', 'author': 'Michelle Obama', 'price': 550, 'stock': 6, 'image_url': 'https://m.media-amazon.com/images/I/81h2gWPTYJL.jpg',"preorder":True},
    {'id': 8, 'title': 'The Alchemist', 'author': 'Paulo Coelho', 'price': 299, 'stock': 14, 'image_url': 'https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg',"preorder":True},
    {'id': 9, 'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman', 'price': 499, 'stock': 4, 'image_url': 'https://m.media-amazon.com/images/I/71f6DceqZAL.jpg',"preorder":True},
    {'id': 10, 'title': 'The Subtle Art of Not Giving a F*ck', 'author': 'Mark Manson', 'price': 349, 'stock': 9, 'image_url': 'https://m.media-amazon.com/images/I/71QKQ9mwV7L.jpg',"preorder":True},
    {'id': 11, 'title': 'Harry Potter and the Sorcerer’s Stone', 'author': 'J.K. Rowling', 'price': 499, 'stock': 20, 'image_url': 'https://m.media-amazon.com/images/I/81YOuOGFCJL.jpg',"preorder":True},
    {'id': 12, 'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'price': 999, 'stock': 8, 'image_url': 'https://m.media-amazon.com/images/I/91dSMhdIzTL.jpg',"preorder":True},
    {'id': 13, 'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'price': 349, 'stock': 11, 'image_url': 'https://m.media-amazon.com/images/I/61-NtNgM1ZL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 14, 'title': 'The Silent Patient', 'author': 'Alex Michaelides', 'price': 399, 'stock': 7, 'image_url': 'https://m.media-amazon.com/images/I/81JJPDNlxSL.jpg',"preorder":True},
    {'id': 15, 'title': 'Normal People', 'author': 'Sally Rooney', 'price': 299, 'stock': 13, 'image_url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1571423190i/41057294.jpg',"preorder":True},
    {'id': 16, 'title': 'Where the Crawdads Sing', 'author': 'Delia Owens', 'price': 449, 'stock': 6, 'image_url': 'https://musicart.xboxlive.com/7/992b6100-0000-0000-0000-000000000002/504/image.jpg',"preorder":True},
    {'id': 17, 'title': '1984', 'author': 'George Orwell', 'price': 249, 'stock': 18, 'image_url': 'https://m.media-amazon.com/images/I/71kxa1-0mfL.jpg',"preorder":True},
    {'id': 18, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'price': 299, 'stock': 20, 'image_url': 'https://cdn.britannica.com/21/182021-050-666DB6B1/book-cover-To-Kill-a-Mockingbird-many-1961.jpg',"preorder":True},
    {'id': 19, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'price': 199, 'stock': 15, 'image_url': 'https://m.media-amazon.com/images/I/81af+MCATTL.jpg',"preorder":True},
    {'id': 20, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'price': 249, 'stock': 12, 'image_url': 'https://m.media-amazon.com/images/I/81A-mvlo+QL.jpg',"preorder":True},
    {'id': 21, 'title': 'The Power of Now', 'author': 'Eckhart Tolle', 'price': 349, 'stock': 14, 'image_url': 'https://www.hachette.co.nz/images/9780733627514.jpg',"preorder":True},
    {'id': 22, 'title': 'Can’t Hurt Me', 'author': 'David Goggins', 'price': 399, 'stock': 10, 'image_url': 'https://covers.storytel.com/jpg-640/9781664994898.5fa1055c-f393-44c6-9043-64fc9371523f?optimize=high&quality=70&width=600',"preorder":True},
    {'id': 23, 'title': 'Deep Work', 'author': 'Cal Newport', 'price': 379, 'stock': 9, 'image_url': 'https://readandblog.com/wp-content/uploads/2023/12/deep-work-book-cover-4.jpg',"preorder":True},
    {'id': 24, 'title': 'Start With Why', 'author': 'Simon Sinek', 'price': 340, 'stock': 7, 'image_url': 'https://images.blinkist.io/images/books/62c43b546cee07000842ea17/1_1/470.jpg',"preorder":True},
    {'id': 25, 'title': 'Grit', 'author': 'Angela Duckworth', 'price': 399, 'stock': 11, 'image_url': 'https://m.media-amazon.com/images/I/71QKQ9mwV7L.jpg',"preorder":True},
    {'id': 26, 'title': 'Man’s Search for Meaning', 'author': 'Viktor E. Frankl', 'price': 350, 'stock': 6, 'image_url': 'https://m.media-amazon.com/images/I/71RC3o90shL.jpg',"preorder":True},
    {'id': 27, 'title': 'The Four Agreements', 'author': 'Don Miguel Ruiz', 'price': 299, 'stock': 15, 'image_url': 'https://bookoutlet.ca/api/image?url=https://images.bookoutlet.com/covers/large/isbn978187/9781878424310-l.jpg&w=3840&q=75',"preorder":True},
    {'id': 28, 'title': 'The 5 AM Club', 'author': 'Robin Sharma', 'price': 375, 'stock': 13, 'image_url': 'https://m.media-amazon.com/images/I/71zytzrg6lL.jpg',"preorder":True},
    {'id': 29, 'title': 'The Mountain Is You', 'author': 'Brianna Wiest', 'price': 329, 'stock': 8, 'image_url': 'https://m.media-amazon.com/images/I/61xivWmExiL.jpg',"preorder":True},
    {'id': 30, 'title': 'The Midnight Library', 'author': 'Matt Haig', 'price': 349, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/81J6APjwxlL.jpg',"preorder":True},
    {'id': 31, 'title': 'Dune', 'author': 'Frank Herbert', 'price': 459, 'stock': 6, 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6Fw36aMARjzrOLQLkxLHJvSrbLc7xjGBq4w&s',"preorder":True},
    {'id': 32, 'title': 'Shantaram', 'author': 'Gregory David Roberts', 'price': 599, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/81s6DUyQCZL.jpg',"preorder":True},
    {'id': 33, 'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'price': 399, 'stock': 12, 'image_url': 'https://m.media-amazon.com/images/I/71UypkUjStL.jpg',"preorder":True},
    {'id': 34, 'title': 'Factfulness', 'author': 'Hans Rosling', 'price': 360, 'stock': 9, 'image_url': 'https://m.media-amazon.com/images/I/71KH-wJcv3L.jpg',"preorder":True},
    {'id': 35, 'title': 'The Lean Startup', 'author': 'Eric Ries', 'price': 380, 'stock': 11, 'image_url': 'https://m.media-amazon.com/images/I/81-QB7nDh4L.jpg',"preorder":True},
    {'id': 36, 'title': 'Rework', 'author': 'Jason Fried & David Heinemeier Hansson', 'price': 340, 'stock': 7, 'image_url': 'https://m.media-amazon.com/images/I/71eXlKpSbmL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 37, 'title': 'Zero to One', 'author': 'Peter Thiel', 'price': 399, 'stock': 8, 'image_url': 'https://m.media-amazon.com/images/I/71m-MxdJ2WL.jpg',"preorder":True},
    {'id': 38, 'title': 'Hooked', 'author': 'Nir Eyal', 'price': 299, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/81L8JOVXJtL.jpg',"preorder":True},
    {'id': 39, 'title': 'Outliers', 'author': 'Malcolm Gladwell', 'price': 369, 'stock': 9, 'image_url': 'https://m.media-amazon.com/images/I/61XsLQzCkRL.jpg',"preorder":True},
    {'id': 40, 'title': 'Blink', 'author': 'Malcolm Gladwell', 'price': 349, 'stock': 6, 'image_url': 'https://m.media-amazon.com/images/I/61tdYH1yHsL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 41, 'title': 'The Code Breaker', 'author': 'Walter Isaacson', 'price': 489, 'stock': 5, 'image_url': 'https://m.media-amazon.com/images/I/61xv3L2LntL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 42, 'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'price': 549, 'stock': 7, 'image_url': 'https://m.media-amazon.com/images/I/81VStYnDGrL.jpg',"preorder":True},
    {'id': 43, 'title': 'Elon Musk', 'author': 'Ashlee Vance', 'price': 450, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/81GqtNbs+PL.jpg',"preorder":True},
    {'id': 44, 'title': 'The Everything Store', 'author': 'Brad Stone', 'price': 399, 'stock': 8, 'image_url': 'https://images.blinkist.io/images/books/5304807a34393700083d0000/1_1/470.jpg',"preorder":True},
    {'id': 45, 'title': 'The Ride of a Lifetime', 'author': 'Robert Iger', 'price': 420, 'stock': 6, 'image_url': 'https://m.media-amazon.com/images/I/71oC2CPfZGL.jpg',"preorder":True},
    {'id': 46, 'title': 'Think Again', 'author': 'Adam Grant', 'price': 369, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/71dJ09pdRkL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 47, 'title': 'The Art of War', 'author': 'Sun Tzu', 'price': 199, 'stock': 15, 'image_url': 'https://m.media-amazon.com/images/I/61lBRY5h+NL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 48, 'title': 'Meditations', 'author': 'Marcus Aurelius', 'price': 250, 'stock': 13, 'image_url': 'https://m.media-amazon.com/images/I/71FCbiv0tTL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 49, 'title': 'The Daily Stoic', 'author': 'Ryan Holiday', 'price': 370, 'stock': 11, 'image_url': 'https://m.media-amazon.com/images/I/71tOgIo1TTL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 51, 'title': 'Born a Crime', 'author': 'Trevor Noah', 'price': 380, 'stock': 9, 'image_url': 'https://www.lowplexbooks.com/cdn/shop/products/OAoDdoPs.jpg?v=1643727377',"preorder":True},
    {'id': 52, 'title': 'Untamed', 'author': 'Glennon Doyle', 'price': 390, 'stock': 10, 'image_url': 'https://m.media-amazon.com/images/I/91nO1nmUErL._UF1000,1000_QL80_.jpg',"preorder":True},
    {'id': 53, 'title': 'Greenlights', 'author': 'Matthew McConaughey', 'price': 420, 'stock': 11, 'image_url': 'https://m.media-amazon.com/images/I/71sBtM3Yi5L.jpg',"preorder":True},
    {'id': 54, 'title': 'The Happiness Project', 'author': 'Gretchen Rubin', 'price': 345, 'stock': 12, 'image_url': 'https://m.media-amazon.com/images/I/81WcnNQ-TBL.jpg',"preorder":True},
    {'id': 55, 'title': 'Lean In', 'author': 'Sheryl Sandberg', 'price': 370, 'stock': 8, 'image_url': 'https://m.media-amazon.com/images/I/81kqrwS1nNL.jpg',"preorder":True}
    
]

preorders = []
exchange_requests = []

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def view_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return "<h2>Book not found</h2>", 404
    return render_template('view_book.html', book=book)

@app.route('/add_to_cart/<int:book_id>')
def add_to_cart(book_id):
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    book_id_str = str(book_id)
    cart[book_id_str] = cart.get(book_id_str, 0) + 1
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_books = []
    for pid, quantity in cart.items():
        for book in books:
            if book['id'] == int(pid):
                book_copy = book.copy()
                book_copy['quantity'] = quantity
                cart_books.append(book_copy)
    return render_template('cart.html', cart_books=cart_books)

@app.route('/remove/<int:book_id>')
def remove(book_id):
    cart = session.get('cart', {})
    cart.pop(str(book_id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    name = request.form['name']
    address = request.form['address']
    city = request.form['city']
    pincode = request.form['pincode']
    upi_id = request.form['upi_id']
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    print("Order received:", name, address, city, pincode, upi_id, latitude, longitude)
    session.pop('cart', None)
    return render_template('thankyou.html', name=name)

@app.route('/payment', methods=['POST'])
def payment():
    session['order_details'] = request.form
    return render_template('payment.html')

@app.route('/gps')
def gps_location():
    return render_template('gps.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()
    searchable_texts = [book['title'].lower() for book in books] + [book['author'].lower() for book in books]
    matches = get_close_matches(query, searchable_texts, n=3, cutoff=0.5)
    results = [book for book in books if book['title'].lower() in matches or book['author'].lower() in matches]
    return {'results': results[:5]}

@app.route('/return/<int:product_id>', methods=['POST'])
def return_product(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        session['cart'] = cart
        flash('Product returned successfully!', 'success')
    else:
        flash('Product not found in cart.', 'error')
    return redirect(url_for('cart'))

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    if request.method == 'POST':
        name = request.form.get('name')
        current_book = request.form.get('current_book')
        if name and current_book:
            exchange_requests.append({'name': name, 'current_book': current_book})
            return redirect(url_for('exchange_requests_page'))
        else:
            return "Missing form data", 400
    return render_template('exchange.html')

@app.route('/exchange-requests')
def exchange_requests_page():
    return render_template('exchange_requests.html', requests=exchange_requests)

@app.route('/preorder/<int:book_id>', methods=['GET', 'POST'])
def preorder_route(book_id):
    book = next((b for b in books if b['id'] == book_id), None)

    if not book:
        flash("Book not found.", "danger")
        return redirect(url_for('index'))

    if not book.get('preorder', False):
        flash("This book is not available for pre-order.", "warning")
        return redirect(url_for('view_book', book_id=book_id))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        if not name or not email:
            flash("Please fill in all the required fields.", "danger")
            return render_template('preorder.html', book=book)

        # Save pre-order
        preorders.append({
            "book_id": book_id,
            "name": name,
            "email": email,
            "title": book['title']
        })

        flash("Your pre-order has been submitted!", "success")
        return render_template('thanks.html', name=name)

    return render_template('preorder.html', book=book)

order_tracking = {
    1001: {
        "order_id": 1001,
        "title": "The Alchemist",
        "status": "Shipped",
        "stages": ["Placed", "Confirmed", "Packed", "Shipped", "Delivered"],
        "delivery_estimate": "July 5, 2025",
        "location": "Bangalore, India",
        "email": "customer1@example.com",
        "phone": "9876543210"
    },
    1002: {
        "order_id": 1002,
        "title": "The Notebook",
        "status": "Delivered",
        "stages": ["Placed", "Confirmed", "Packed", "Shipped", "Delivered"],
        "delivery_estimate": "July 2, 2025",
        "location": "Mumbai, India",
        "email": "customer2@example.com",
        "phone": "9876501234"
    }
}

@app.route('/')
def home():
    return redirect(url_for('track'))

@app.route('/track', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        return redirect(url_for('track_order', order_id=order_id))
    return render_template('track_form.html')

@app.route('/track_order/<int:order_id>')
def track_order(order_id):
    order = order_tracking.get(order_id)
    if not order:
        return "Order not found", 404

    # Simulated email and SMS logs
    tracking_url = request.url
    print(f"[EMAIL] Sent to {order['email']}: Track your order here: {tracking_url}")
    print(f"[SMS] Sent to {order['phone']}: Track your order here: {tracking_url}")

    return render_template('track_order.html', order=order)



if __name__ == '__main__':
    app.run(debug=True)
