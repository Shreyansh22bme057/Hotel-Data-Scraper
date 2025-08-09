# 🏨 Booking.com Hotel Data Scraper

A Python-based web scraping tool that extracts hotel details from **Booking.com** search result pages using **BeautifulSoup** and **Requests**.

## 🚀 Features

- Scrapes hotel information such as:
  - Hotel Name
  - Location
  - Distance from city center (Reach)
  - Score
  - Rating
  - Number of Reviews
  - Booking link
- Saves extracted data into a CSV file.
- Uses a custom **User-Agent** header to avoid basic blocking.
- Allows dynamic URL input for different search queries.

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – For sending HTTP requests.
- **BeautifulSoup4** – For parsing and extracting HTML content.
- **lxml** – For fast HTML parsing.
- **CSV** – For saving scraped data.

## 📦 How to Use

1. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4 lxml
2. **Run the script**:
   ```bash
   python scrapper_code.py
3. **Provide input when prompted**:
Paste the Booking.com search results URL (must be a valid page).
Enter a file name for the CSV output.

4.**View results**:
The output CSV file will be saved in the same directory.
