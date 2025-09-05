# News Summarizer

## Overview
The **News Summarizer** is a Django-based web application designed to extract and summarize news articles from various online sources. It leverages natural language processing (NLP) techniques to generate concise summaries, enabling users to quickly understand the key points of news articles. The application provides a user-friendly web interface for inputting article URLs and viewing summaries.

## Features
- **Article Extraction**: Fetches news articles from provided URLs or external APIs.
- **Text Summarization**: Uses NLP algorithms to produce concise and accurate summaries.
- **Customizable Summaries**: Allows users to specify summary length or other parameters.
- **Web Interface**: Built with Django templates for an intuitive user experience.
- **API Integration**: Supports integration with news APIs for fetching articles (configured in `utils.py`).
- **Scalable Design**: Modular structure with Django's app-based architecture.

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

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
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
