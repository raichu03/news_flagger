from sentence_transformers import SentenceTransformer, util
import numpy as np

def calculate_semantic_similarity_score(claims1, claims2, similarity_threshold=0.5):
    """
    Calculates a single, final similarity score between two lists of claims based on the average of
    ALL scores that are above the similarity threshold.

    Args:
        claims1 (list): A list of dictionaries, where each dictionary represents a claim.
        claims2 (list): A second list of dictionaries, representing claims to compare against.
        similarity_threshold (float): The minimum cosine similarity score to consider two claims as a match.
                                      A value between 0 and 1. A higher value means a stricter match.

    Returns:
        float: A single similarity score between 0 and 1, where 1 indicates high semantic similarity
               and 0 indicates no similarity above the threshold.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')


    
    
    # Extract claim texts from the dictionaries
    claim_texts1 = [claim['claim'] for claim in claims1['claims']]
    claim_texts2 = [claim['claim'] for claim in claims2['claims']]

    # Handle cases where one or both lists are empty
    if not claim_texts1 or not claim_texts2:
        return 0.0

    # Encode the claim texts into embeddings
    embeddings1 = model.encode(claim_texts1, convert_to_tensor=True)
    embeddings2 = model.encode(claim_texts2, convert_to_tensor=True)

    total_score = 0
    num_matched_claims = 0

    # Iterate through each claim in the first list
    for i, claim1_text in enumerate(claim_texts1):
        claim1_embedding = embeddings1[i]
        
        # Calculate cosine similarity with all claims in the second list
        similarities = util.cos_sim(claim1_embedding, embeddings2)

        # Iterate through ALL similarity scores for the current claim
        for score in similarities[0]:
            # If the score is above the threshold, include it in the calculation
            if score >= similarity_threshold:
                total_score += score
                num_matched_claims += 1

    # Calculate the average score
    if num_matched_claims > 0:
        final_score = total_score / num_matched_claims
        return final_score.item()  # Convert tensor to float
    else:
        return 0.0