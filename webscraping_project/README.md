**🛒 ShopEase – Web Scraping Project**

📌 Description :

ShopEase is a Flask-based web application that scrapes product data from real online sources, stores it in a SQLite database, and displays the data through a searchable web interface.

The project uses both API scraping and HTML web scraping while excluding grocery and food items.

🌐 Data Sources :

DummyJSON API – Product data (electronics, fashion, etc.)

Books to Scrape – Book data using HTML scraping

🧰 Technologies Used :

Python

Flask

SQLite

Requests

BeautifulSoup

HTML, CSS, Jinja2

📁 Project Structure :

webscraping_project/
│
├── app.py
├── fetch_data.py
├── products.db
│
├── templates/
│   ├── index.html
│   └── product.html
│
└── static/
    └── style.css

⚙️ Features :

Real web scraping (API + HTML)

SQLite database storage

Product search functionality

Category filtering

Product detail page

▶️ How to Run:

pip install flask requests beautifulsoup4
python fetch_data.py
python app.py


Open in browser :

http://127.0.0.1:5000

🖼️ Note on Images :

Some product images may not load due to CDN protection on real websites.
This is expected and not a code issue.

🎓 Purpose :

This project is developed for educational use only to demonstrate web scraping, database handling, and Flask web development.
