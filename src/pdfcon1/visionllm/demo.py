from openai import OpenAI
import base64
import os

def encode_image(image_path):
    '''Encodes am image to base 64 string'''
    with open(image_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

client = OpenAI()

cwd = os.getcwd()
image_path =  cwd+"/src/pdfcon1/data/image.png"
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': 'is this has a offcial stand and signature'
                },
                {
                   'type': 'image_url',
                   'image_url': 
                   {
                    #    'url': 'https://site/image.jpg',
                    'url': f'data:image/png;base64,{base64_image}',
                   },

                },
            ],
        }
    ],
    max_tokens=300
)

print(response.choices[0].message)
# print("completion tokens: ", response.usage.completion_tokens)
# print("Prompt tokens: ", response.usage.prompt_tokens)
# print("total token: ", response.usage.total_tokens)
