import base64
import re

def encode_image(image_path):
    '''Encodes am image to base 64 string'''
    with open(image_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

def extract_code(text):
    pattern = r'```python\s+(.*?)\s+'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    return None