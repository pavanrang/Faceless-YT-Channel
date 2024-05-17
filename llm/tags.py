from openai import OpenAI
import json
import re
from typing import List
from termcolor import colored

def get_search_terms(video_subject,amount,script):
    prompt = f"""
    Generate {amount} search terms for stock videos,
    depending on the subject of a video. Reply in English Only.
    Subject: {video_subject}

    The search terms are to be returned as
    a JSON-Array of strings.

    Each search term should consist of 1-3 words, 
    always add the main subject of the video.

    Here is an example of a JSON-Array of strings:
    ["search term 1", "search term 2", "search term 3"]

    Obviously, the search terms should be related
    to the subject of the video.

    ONLY RETURN THE JSON-ARRAY OF STRINGS.
    DO NOT RETURN ANYTHING ELSE.

    For context, here is the full text:
    {script}
    """
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key="api key"
    )
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user","content": prompt}]
    )
    
    search_terms = response.choices[0].message.content
    return search_terms
