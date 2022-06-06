# news-scaper

Project consists of codes for scraping articles from various news providers.

## 1. Google News Scraper

GoogleNewsScraper scrapes articles from google news rss feeds based on the given query.

### Project Directory Structure

```
  ├── news-scaper                           # Root Folder
    ├── src/                                # Source Code directory
      ├── GoogleNewsScaper/                 # Google News Scaper directory
        ├── BasicScaper.ipynb               # IPython notebook consists of basic code for scraping google news.
        ├── GoogleNewsScaper.py             # Python script file consists of code for scraping google news for the given query.
        ├── GoogleNewsScaper.ipynb          # IPython notebook consists of code for scraping google news for the given query.
    ├── .gitignore                          # .gitignore file
    ├── requirements.txt                    # Library dependencies
```

## Installation

1. Clone the repository into a folder
```
git clone git@github.com:kishore-s-15/news-scaper.git
```

2. Change the directory to the project root directory.

3. Create a virtual environment

   > On Windows run
   ```
   python -m venv .venv
   ```
   
   > On Linux and MacOs run
   ```
   python3 -m venv .venv
   ```

4. Activate the virtual environment

   > On Windows run
   ```
   .venv\Scripts\activate.bat
   ```
   
   > On Linux and MacOs run
   ```
   source .venv/bin/activate
   ```
   
5. Install the dependencies for the project in the virtual environment
```
pip install -r requirements.txt
```
   
6. Then run the following command

   > On Windows run
   ```
   python src\GoogleNewsScaper\GoogleNewsScaper.py
   ```
   
   > On Linux and MacOs run
   ```
   python3 src/GoogleNewsScaper/GoogleNewsScaper.py
   ```

This should start scraping the news articles and print it out to the console.
