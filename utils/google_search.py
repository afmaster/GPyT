from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import html2text
from googlesearch import search

def search_google(query: str) -> str:
    """
    Search and retriev the text content from the first result of Google engine.
    :param query: user_input
    :return: text from html of the Google first result page.
    """
    for url in search(query, num_results=1):
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        soup = BeautifulSoup(html, features="html.parser")
        extractedText = soup.get_text()
        h = html2text.HTML2Text()
        h.ignore_links = True
        blogPost = h.handle(extractedText)
        print(blogPost)
        return blogPost

