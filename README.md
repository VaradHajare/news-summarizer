# News Summarizer

## Overview
<img width="1881" height="907" alt="image" src="https://github.com/user-attachments/assets/2e06d47c-aecf-4a58-85ec-6ba9b00ca484" />

The **News Summarizer** is a Django web app that aggregates latest news from multiple sources via NewsAPI, uses AI transformers to summarize full articles, and displays clean, readable news with citations in a dark-themed, user-friendly interface.

## Features
- Aggregates latest news from multiple sources using NewsAPI
- Supports news search with language filtering
- Extracts and parses full article content using Newspaper3k
- Summarizes news articles using AI transformer models (distilbart-cnn-12-6)
- Displays news headlines with author, source, and publish date citations
- Opens full articles in a clean, dark-themed popup reader mode with scrollable content
- Easy customization of language, summarization model, and news filters in code

## Project Structure
```
news-summarizer/
│
├── manage.py                  
├── newsanalyzer/            
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          
│   ├── urls.py               
│   ├── wsgi.py
├── news/                     
│   ├── migrations/          
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py              
│   ├── apps.py              
│   ├── models.py            
│   ├── tests.py             
│   ├── urls.py               
│   ├── utils.py              
│   ├── views.py              
│   └── templates/
│       └── news/
│           └── home.html    
├── requirements.txt          
└── README.md                
```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VaradHajare/news-summarizer.git
   cd news-summarizer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://localhost:8000`.

## Usage
1. **Access the Web Interface**:
   - Open a browser and navigate to `http://localhost:8000`.
   - Enter the URL of a news article in the provided input field on the `home.html` page.
   - Adjust summary length or other parameters (if available).
   - Submit to view the generated summary.

2. **API Integration** (Optional):
   - Configure API keys in `newsanalyzer/settings.py` or `news/utils.py` for external news APIs (e.g., NewsAPI).
   - Update `utils.py` to fetch articles programmatically if needed.

3. **Admin Panel**:
   - Create a superuser to access the Django admin panel:
     ```bash
     python manage.py createsuperuser
     ```
   - Access the admin panel at `http://localhost:8000/admin` to manage models or data.

## Requirements
- Python 3.8+
- Django 4.0+
- Other dependencies listed in `requirements.txt` (e.g., `requests`, `nltk`, `beautifulsoup4`, etc.)

## Configuration
- **Settings**: Modify `newsanalyzer/settings.py` to configure database, API keys, or other settings.
- **Summarization Logic**: Customize summarization algorithms in `news/utils.py`.
- **Frontend**: Update `news/templates/news/home.html` for UI changes.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, reach out to [Varad Hajare](https://github.com/VaradHajare) or open an issue on this repository.
