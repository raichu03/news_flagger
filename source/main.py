from utils import make_custom_search, extract_text_from_class, extract_text_from_url, generate_headline, extract_sources_and_claims, compare_articles


def main(article_url):
    ### Extracting the news artilce form the kathmandu post ###
    original_article = extract_text_from_class(url=article_url)
    
    original_headline = original_article['headline']
    new_headline = generate_headline(original_headline)
    
    ### This code uses websearch to find the similar articles ###
    ### Its better to search only in the local news websites  ###
    similar_article_list = make_custom_search(query=new_headline)
    
    ### These are the test articles ###
    # similar_article_list = ['https://en.setopati.com/political/164318', 'https://mypeoplesreview.com/2025/07/26/former-prez-bhandari-defends-her-uml-membership/', 'https://mypeoplesreview.com/2025/07/24/chair-oli-toughens-stance-bhandari-barred-from-party-politics/']
    all_articles = []
    for url in similar_article_list:
        
        secondary_article = extract_text_from_url(url=url)
        all_articles.append(secondary_article)
    
    original_claims = extract_sources_and_claims(article_text=original_article['article'])
    
    all_claims = []
    for articles in all_articles:
        secondary_claims = extract_sources_and_claims(articles)
        all_claims.append(secondary_claims['claims'])
    
    all_scores = compare_articles(original_claims['claims'], all_claims)
    
    average = sum(all_scores) / len(all_scores)
    return average


if __name__=="__main__":
    
    ### Add your article link here ###
    ### This code only supports kathmandu post ###
    article_url = 'https://kathmandupost.com/politics/2025/07/23/bidya-bhandari-s-political-adventurism-hits-a-brake-for-now'
    
    average_score = main(article_url)
    print(average_score)