from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import datetime
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

Bootstrap5(app)

year = datetime.datetime.now().year

def convert_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def create_colors(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    # color is in bgr format so we have to change it to rgb format
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


def get_colors(image, code):

    try:
        img = cv2.imread(image)
        height, width, _ = np.shape(img)


        # Reshape the image for clustering
        data = np.reshape(img, (height*width, 3))
        # Change it into float type
        data = np.float32(data)

        # Define the number of clusters we want
        number_clusters = 10

        # Defining algorithm termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

        bars = []
        rgb_values = []

        for index, row in enumerate(centers):
            bar, rgb = create_colors(200, 200, row)
            bars.append(bar)
            rgb_values.append(rgb)

        if code == "hex":
            hex_list = []
            for value in rgb_values:
                hex_code = convert_to_hex(value)
                hex_list.append(hex_code)
            return hex_list
        else:
            return rgb_values

    except Exception as e:
        return f"Error processing image: {str(e)}"

    # img_bar = np.hstack(bars)
    # cv2.imshow('Dom Colors', img_bar)
    #
    # cv2.waitKey(0)


@app.route("/", methods=['GET', 'POST'])
def home():
    default_image_path = os.path.join(app.config['UPLOAD'], 'ccoral.png')
    color_default = get_colors(default_image_path, "hex")
    code_default = "hex"

    error = None

    if request.method == 'POST':
        try:
            file = request.files['image']
            default_image = "/static/img/ccoral.png"
            if not file:
                error = "No file uploaded"
                raise ValueError(error)
            filename = secure_filename(file.filename)

            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                error = "Unsupported file type. Please upload a PNG or JPG image."
                raise ValueError(error)

            file.save(os.path.join(app.config['UPLOAD'], filename))
            image = os.path.join(app.config['UPLOAD'], filename)
            color_code = request.form.get('color_code', False)
            colors = get_colors(image, color_code)
            return render_template('index.html', colors_list=colors,
                                   code=color_code, image=image, error=error, year=year)

        except ValueError as e:
            error = str(e)
        except FileNotFoundError:
            error = "File not found. Please select an image"

    return render_template('index.html', image="/static/img/ccoral.png", error=error,colors_list=color_default, code= code_default,year=year)


# @app.route("/try", methods=['GET', 'POST'])
# def try_out():
#     # color_default = get_colors("ccoral.png", "rgb")
#     default_image_path = os.path.join(app.config['UPLOAD'], 'ccoral.png')
#     color_default = get_colors(default_image_path, "hex")
#     code_default = "hex"
#     error = None
#
#     if request.method == 'POST':
#         file = request.files['image']
#         if not file:
#             error = "No file uploaded"
#         filename = secure_filename(file.filename)
#
#         if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#             error =  "Unsupported file type. Please upload a PNG or JPG image."
#
#         file.save(os.path.join(app.config['UPLOAD'], filename))
#         image = os.path.join(app.config['UPLOAD'], filename)
#         color_code = request.form.get('color_code', False)
#         colors = get_colors(image, color_code)
#
#         return render_template('try.html', colors_list=colors,
#                                code=color_code, image=image)
#
#     return render_template('try.html', image="/static/img/ccoral.png", error=error,colors_list=color_default ,code=code_default,year=year)


@app.errorhandler(500)
def handle_error(error):
    return render_template('index.html', error="An unexpected error occurred. Please try again."), 500


if __name__ == "__main__":
    app.run(debug=True)

