from .sources import extract_sources_and_claims
from .similarity import calculate_semantic_similarity_score

def compare_articles(original: str, secondary: list):
    
    original_claims = extract_sources_and_claims(article_text=original)
    
    all_scores = []
    for articles in secondary:
        secondary_claims = extract_sources_and_claims(articles)
        
        score = calculate_semantic_similarity_score(original_claims, secondary_claims)
        
        all_scores.append(score)
        
    return all_scores