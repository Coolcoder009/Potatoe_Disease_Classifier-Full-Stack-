# Leaf Guard - Potato Disease Classifier

Leaf Guard is a project designed to classify potato diseases from images using a Convolutional Neural Network (CNN) model. It provides an intuitive web interface where users can upload potato leaf images for disease prediction.

## Installation

1. Clone the repository 
```bash 
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

3. To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

4. To run this project backend:
```bash 
uvicorn main:app --reload
```

### Algorithms and Models Used

The project leverages the following technologies and libraries:

#### FastAPI: 
FastAPI is used to create the web application that serves as the API endpoint for image uploads and predictions.

#### TensorFlow: 
TensorFlow is employed to load and utilize the pre-trained CNN model for image classification.

#### NumPy: 
NumPy handles numerical operations and array manipulations.

#### PIL (Python Imaging Library): 
PIL is used for image resizing and manipulation.

### Model Details
CNN Model: The core of the project is a Convolutional Neural Network (CNN) model trained on a dataset of potato leaf images. The model architecture is designed to classify these images into specific disease categories.
Prediction Endpoint
Endpoint: The /predict/ endpoint of the FastAPI application accepts POST requests with uploaded potato leaf images.
Processing: Upon receiving an image, the application preprocesses it, passes it through the CNN model, and returns the predicted disease category.
Output: Predictions are returned as JSON responses containing the predicted class (e.g., "Early Blight", "Late Blight", "Healthy").

## Running the Application
To use the Potato Disease Classifier:
<ul>
<li>Upload Image: Visit the deployed FastAPI application or run it locally. Upload a potato leaf image via the provided interface.</li>
<li>Receive Prediction: After uploading, the application processes the image and provides a prediction of the disease category.</li>
<li>Example Usage
<li>Local Development: Run the FastAPI server locally to test the application with sample images.</li>
<li>Deployment: Deploy the application to a cloud platform or server for wider accessibility.</li>
</ul>

## Future Enhancements

Improve model accuracy through additional data augmentation and training.
Enhance the user interface for easier image uploading and feedback.

