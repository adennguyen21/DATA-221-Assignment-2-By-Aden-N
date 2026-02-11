# Question 7 - Extracting structured content from a webpage.
#==================================================================================

import requests
from bs4 import BeautifulSoup


def load_soup(data_url):
    # Scraps the wiki website and put the data into one big "soup".
    headers = {"User-Agent": "Mozilla/5.0"}
    wiki_contents = requests.get(data_url, headers=headers)
    return BeautifulSoup(wiki_contents.text, "html.parser")


def get_page_title(soup):
    # Finds the page title and prints it out.
    page_title = soup.find("title")
    page_title = page_title.text

    print(f"The Page title is: '{page_title}'")


def get_first_paragraph(soup):
    # Finds the first paragraph from the main content, and prints it out.
    # (Printing was not needed but I put it in to show.)
    wiki_text_content = soup.find("div", id="mw-content-text")
    all_paragraphs = wiki_text_content.find_all("p")

    first_valid_paragraph = None

    for paragraph in all_paragraphs:
        testing_text = paragraph.get_text(strip=True)
        testing_text = testing_text.replace(" ", "")

        if len(testing_text) >= 50:
            first_valid_paragraph = paragraph.text
            break

    print(f"The first paragraph from the main article is: \n{first_valid_paragraph}")

# ======================================================================================

def main():
    wiki_page = "https://en.wikipedia.org/wiki/Data_science"

    data_science_soup = load_soup(wiki_page)

    get_page_title(data_science_soup)

    print()

    get_first_paragraph(data_science_soup)

main()