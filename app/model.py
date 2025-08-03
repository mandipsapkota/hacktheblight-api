from transformers import pipeline
from PIL import Image
import torch

# Load the model only once
classifier = pipeline("image-classification", model="linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")

def predict(image: Image.Image):
    result = classifier(image)
    return result
