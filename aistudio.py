# pip install google-genai

from google import genai


# def generate():
client = genai.Client(
    api_key="AIzaSyDgy9F_jAiKc3_URCEAZjxu-xVxhtcM5RI",
)

MODEL = 'gemini-2.5-flash'
PROMPT = 'write essay on of Apple fruit? '
response = client.models.generate_content(
    model=MODEL,
    contents=PROMPT,
    config=genai.types.GenerateContentConfig(
        # thinking_config=genai.types.ThinkingConfig(thinking_budget=50),
        # max_output_tokens=200,
        temperature=0,
        top_p=1,
        
    )
    
)

input_token_count=client.models.count_tokens(model=MODEL, contents=PROMPT)

# print(input_token_count.total_tokens)
print(response.text)
print('total_token_count ',response.usage_metadata.total_token_count)
print('candidates_token_count ', response.usage_metadata.candidates_token_count)
print('thoughts_token_count ',response.usage_metadata.thoughts_token_count)
print('prompt_token_count ',response.usage_metadata.prompt_token_count)

