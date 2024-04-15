import re
import requests

def extract_urls_from_web_page(url):
    # Fetch the web content
    response = requests.get(url)
    text = response.text

    # Regular expression for URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    return urls



if __name__ == "__main__":
    web_page_url = input("Enter the URL of the web page: ")
    urls = extract_urls_from_web_page(web_page_url)
    print("The URLs in the web page are:")
    for url in urls:
        print(url)
    
