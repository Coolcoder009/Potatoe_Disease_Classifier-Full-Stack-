from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from io import BytesIO
from PIL import Image
import numpy as np
import tensorflow as tf

app = FastAPI()

# Adjust CORS settings as necessary
origins = ["*"] # This allows all origins for simplicity

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Adjust as per your requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the TensorFlow model directly
model_path = "C:/Users/Welcome/Desktop/Potato_Disease_Classification/potatoes.h5"  # Update this path to your model's path
model = tf.keras.models.load_model(model_path)

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((256, 256))  # Adjust the size as per your model's requirement
    return np.array(image)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    image = np.expand_dims(image, axis=0)  # Model expects a batch of images

    prediction = model.predict(image)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    
    return {"class": predicted_class}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

