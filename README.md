# Image Color Extractor
![Image Color Extractor](https://github.com/user-attachments/assets/da132dcb-bdfa-45e0-8b54-7f110fc55f1b)

This project is a web application built with Flask that extracts the dominant colors from an uploaded image using k-means clustering. The app returns the top 10 colors in either RGB or HEX format, which can be useful for design, analysis, and inspiration.
## Features
* Upload an image (PNG, JPG, or JPEG).
* Extract the dominant colors from the image.
* Display the colors as colored bars.
* Optionally, choose to display the colors in HEX or RGB format.
* Bootstrap styling for responsive, modern UI.
* **Copy code functionality**: Users can copy the code directly to their clipboard by clicking the "Copy" button below the code block.

## Installation
Follow these steps to run the project locally:

## Prerequisites
Make sure you have Python 3 installed. Then, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
## Running the Application
1.Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/image-color-extractor.git
cd image-color-extractor
```
2. Install the necessary Python packages:
```bash
pip install -r requirements.txt
```
3. Run the application using Flask's built-in server:
```bash
python app.py
```
4. Visit the app in your browser at http://localhost:5000.

## How It Works
### Upload Image
* Open the application in your browser.
* Upload an image file (PNG, JPG, or JPEG).
* Optionally, choose whether to display the colors in HEX or RGB format.
* The top 10 dominant colors will be displayed as color bars, along with their corresponding color codes.
## Color Extraction Logic
The application uses k-means clustering to extract the dominant colors from the uploaded image. The image is reshaped into a 2D array, and the k-means algorithm is applied to find the centroids of the most common colors. These colors are then displayed in the UI.

## Color Code Formats
You can choose to display the extracted colors in RGB or HEX format. The colors are converted accordingly:

* **RGB**: A tuple of values representing Red, Green, and Blue.
* **HEX**: A hexadecimal string representing the color code.
## Dependencies
The project uses the following Python packages:

* **Flask**: Web framework to build the application.
* **Flask-Bootstrap**: For integrating Bootstrap 5 into Flask.
* **opencv-python**: For image processing and color extraction.
* **numpy**: For numerical operations and image array manipulations.
* **werkzeug**: For secure file handling.
