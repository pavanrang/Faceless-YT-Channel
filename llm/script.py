from openai import OpenAI
from langchain.prompts import PromptTemplate

def Groq(query):
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key="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"
    )
    try:
        llm_response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user","content": query}],
            temperature=0.2,
            max_tokens=1024,
            top_p=1,
            stop=None,
        )
        return llm_response
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def generate_video_script(video_subject):
    prompt_template = """
        Generate a script for a video, depending on the subject of the video.
        The script is youtube shorts.
        Duration of youtube short is typically 40-50 seconds.
        Generate script for a youtube short video.
        The script Should be Entartaining or else viewer skips the video.
        
        Subject: {video_subject}

        The script is to be returned as a string.

        Here is an example of a string:
        "This is an example string."

        Do not under any circumstance refernce this prompt in your response.

        Get straight to the point, don't start with unnecessary things like, "welcome to this video".

        Obviously, the script should be related to the subject of the video.

        ONLY RETURN THE RAW SCRIPT. DO NOT RETURN ANYTHING ELSE.
        No Emojis
        """
    prompt = PromptTemplate(input_variables=["video_subject"], template=prompt_template)
    prompt_with_input = prompt.format(video_subject=video_subject)

    response = Groq(prompt_with_input)
    if response:
        return response.choices[0].message.content