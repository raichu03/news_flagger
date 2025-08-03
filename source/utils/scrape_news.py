import requests

from bs4 import BeautifulSoup
from newspaper import Article

def extract_text_from_class(url):
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        article = Article(url)
        
        article.download()
        article.parse()
        
        article_title = article.title
        published_date = article.publish_date
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_body = soup.find(class_='story-section')
        extracted_article = article_body.get_text(strip=True)
        
        article_author = soup.find(class_='text-capitalize')
        extracted_author = article_author.get_text(strip=True)
        
        article_date = soup.find(class_='updated-time')
        extracted_date = article_date.get_text(strip=True)
        
        return {
            'headline': article_title,
            'author': extracted_author,
            'date': published_date,
            'article': extracted_article
        }
        
    except requests.exceptions.RequestException as e:
        return {'error': f"Request failed: {str(e)}"}
    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}