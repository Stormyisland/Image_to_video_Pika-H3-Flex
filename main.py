
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="wavespeed",
    api_key=os.environ["HF_TOKEN"],
)

with open("cat.png", "rb") as image_file:
   input_image = image_file.read()
