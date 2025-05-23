#!/usr/bin/env python
import sys
import warnings
from PIL import Image

from datetime import datetime

from pdfcon1.crew import Pdfcon1
import os
import base64

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def encode_image_to_base64(image_path):
    """
    Encodes an image file to a Base64 string.

    Args:
        image_path: The path to the image file.

    Returns:
        A Base64 encoded string of the image, or None if an error occurs.
    """
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded_data = base64.b64encode(image_data)
            base64_string = base64_encoded_data.decode("utf-8")
            # return base64_string
            return base64_string
        
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    


def run():
    """
    Run the crew.
    """

    # image_path = "/Users/aswarna/pdfcon1/src/pdfcon1/data/Hello.jpeg" 
    # base64_string = encode_image_to_base64(image_path)

    

    # img = Image.open("/Users/aswarna/pdfcon1/src/pdfcon1/data/Hello.jpeg")
    # img = "https://m.media-amazon.com/images/M/MV5BNDUwNjBkMmUtZjM2My00NmM4LTlmOWQtNWE5YTdmN2Y2MTgxXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg"

    inputs = {
        # 'topic': 'AI LLMs',
        # 'current_year': str(datetime.now().year)
        # 'image': base64_string
        'image_url':'/Users/aswarna/pdfcon1/src/pdfcon1/data/image.png'
    }

    # print(type(base64_string))
    # print(base64_string)
    
    try:
        Pdfcon1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Pdfcon1().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Pdfcon1().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Pdfcon1().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


# if __name__ == '__main__':
#     image_path = "/Users/aswarna/pdfcon1/src/pdfcon1/data/Hello.jpeg" 
#     base64_string = encode_image_to_base64(image_path)
#     print(len(base64_string))
