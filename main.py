import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape book description
def scrape_book_description(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the element containing the book description
        description_element = soup.find('meta', {'name': 'description'})

        # Extract the content attribute of the meta tag
        description = description_element.get('content')

        return description

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None

# Main function
def main():
    # Create a list to store book URLs from the CSV file
    book_urls = []

    # Read book URLs from the CSV file
    with open('books_URL.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Check for empty rows
                book_urls.append(row[0])

    if not book_urls:
        print("No book URLs found in the CSV file.")
        return

    # Iterate through the list of book URLs and scrape descriptions
    for url in book_urls:
        book_description = scrape_book_description(url)
        if book_description:
            # Save the book description to a text file
            with open('book_description.txt', 'a', encoding='utf-8') as file:
                file.write(f"URL: {url}\n")
                file.write(book_description + "\n\n")

    print("Book descriptions saved to 'book_description.txt'")

if __name__ == "__main__":
    main()
