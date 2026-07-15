# Example: Hugging Face API ka chhota sa code
import requests

def generate_image_free(prompt):
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"} # HuggingFace ki free key
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.content
