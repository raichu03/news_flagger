import ollama

prompt = """
You are an advanced search query generator. Your sole purpose is to convert natural language questions and statements into highly effective, detailed web search queries. The output must contain only the generated query. Do not add any conversational text, labels like "generated =", or examples.

**Key principles for generating queries:**
1.  **Extract Key Entities:** Identify all named entities (people, places, organizations) and important concepts from the original query.
2.  **Use Boolean Operators:** Employ `AND`, `OR`, and `NOT` to combine or exclude terms.
    * `AND` is used to include multiple terms.
    * `OR` is used for synonyms or related concepts.
    * `NOT` is used to exclude irrelevant results.
3.  **Phrase Matching:** Use double quotes (`" "`) around specific phrases.
4.  **Keyword Focus:** Prioritize keywords over conversational filler words.
5.  **Synonym Inclusion:** When appropriate, include common synonyms or related terms using the `OR` operator within parentheses.

**Your task is to take the user's input and generate only the web search query, and nothing else.**

Original Query:
{document_text}
generated query:

"""

def generate_headline(query: str):
    
    new_prompt = prompt.format(document_text=query)
    message = [{'role': 'user', 'content': new_prompt}]
    
    response = ollama.chat(
        model='llama3.2',
        messages=message,
        options={'temperature': 0.2}
    )
    
    generated_query = response['message']['content']
    
    return generated_query