import requests
from bs4 import BeautifulSoup
import csv

def scrape_to_csv(url, csv_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [h2.text.strip() for h2 in soup.find_all("h2")]
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title"])
        for title in titles:
            writer.writerow([title])
    print("✅ Data saved to", csv_file)

# Example usage
# scrape_to_csv("https://example.com/blog", "titles.csv")
