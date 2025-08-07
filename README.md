# Link Collector App

A simple Django web application for collecting and displaying links from a given URL. This project was created for learning purposes.

## Features
- Enter a website URL and scrape links from the page
- Display scraped links in a responsive Bootstrap table
- Simple, clean UI using Bootstrap 5

## Screenshots
![App Screenshot](screenshot.png)

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/scraper.git
   cd scraper
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and go to `http://127.0.0.1:8000/`

## Usage
- Enter a website URL in the input field and click "Scrape".
- The app will display a table of links found on the page.

## Project Structure
```
mysite/
├── manage.py
├── db.sqlite3
├── mysite/
│   └── ...
└── myapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── myapp/
    │       └── result.html
    └── ...
```

## License
This project is for educational purposes only.
