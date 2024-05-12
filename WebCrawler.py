import requests
from bs4 import BeautifulSoup


class WebCrawler:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an exception for error responses
        return response.content

    def parse_html(self, html_content):
        return BeautifulSoup(html_content, "html.parser")

    def extract_information(self, soup):
        # Implement your specific extraction logic here
        raise NotImplementedError("Subclasses must implement this method")


class ExampleCrawler(WebCrawler):
    def extract_information(self, soup):
        # Example: Extract paragraphs and links
        paragraphs = soup.find_all("p")
        links = soup.find_all("a")
        return paragraphs, links


# Test usage:
if __name__ == "__main__":
    crawler = ExampleCrawler("")  # Replace with your target URL
    html_content = crawler.fetch_html()
    print(html_content)
    soup = crawler.parse_html(html_content)
    paragraphs, links = crawler.extract_information(soup)

    # Process extracted data as needed
    print("Paragraphs:")
    for paragraph in paragraphs:
        print(paragraph.text.strip())

    print("\nLinks:")
    for link in links:
        print(link.get("href"))



