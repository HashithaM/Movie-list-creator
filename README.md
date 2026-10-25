# Web Scraping and Movie List Experiments

A Python learning project exploring HTML parsing and browser-assisted scraping. The script first demonstrates Beautiful Soup selectors with a local HTML file and Hacker News, then attempts to collect movie titles from an Empire page and save them to `movies.txt`.

## What it demonstrates

- Parsing local and remote HTML with Beautiful Soup
- CSS-style and attribute-based element selection
- Collecting titles, links, and vote counts
- Identifying the most-upvoted Hacker News item
- Using headless Selenium for JavaScript-rendered pages
- Writing extracted movie titles to a text file

## Requirements

```bash
pip install beautifulsoup4 lxml requests selenium
```

## Run

```bash
python main.py
```

Google Chrome and a compatible driver are required for the Selenium section.

## Notes

The source combines several course exercises in one file and relies on page structures that may change. Review each target site's terms and robots policy before scraping, and update selectors when the source pages change.
