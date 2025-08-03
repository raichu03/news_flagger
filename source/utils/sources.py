import ollama
import json

def extract_sources_and_claims(article_text):
    prompt = f"""
    Analyze the following news article and extract all key claims and their sources.
    For each claim, identify the person, organization, or government body responsible for the statement.
    Format the output as a JSON list of objects, with each object containing:
    - 'claim': The statement or key information.
    - 'source': The person, organization, or government body that made the claim.
    - 'type': 'Individual', 'Organization', or 'Government Body'.
    
    ** You do not need to create a list of objects for all the statement, just for the most important events and claims that might be in public interest

    Article:
    {article_text}

    JSON Output:
    """
    
    message = [{'role': 'user', 'content': prompt}]
    
    response = ollama.chat(
        model='llama3.2',
        messages=message,
        options={'temperature': 0.2},
        format='json'
    )
    
    json_response = json.loads(response['message']['content'])
    
    return json_response