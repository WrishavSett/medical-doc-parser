import os
from google import genai
from PIL import Image
import time

# 1. Setup
os.environ["GEMINI_API_KEY"] = "AIzaSyCPkltG2AwO6rCoysPXzuCgPIviLVStq1w"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Load your image
image1 = Image.open(f"./src/tabledata.png")
image2 = Image.open(f"./src/textdata.png")

# 3. Initialize your prompt
prompt="""
Read the image.
Extract all the data from it and give a JSON response.
"""

# 4. Hit Google AI Studio API
def response_gen(image, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            image,
            prompt
        ]
    )

    return response

# 5. Output
def main():

    time.sleep(3)
    response = response_gen(image1, prompt)
    print(response.text)

    time.sleep(3)
    response = response_gen(image2, prompt)
    print(response.text)

if __name__ == "__main__":
    main()