# Background Remover Web App

This is a simple web application built with Flask that allows users to remove the background from images. It utilizes the `rembg` library for background removal.

## Prerequisites

- Python 3.x
- Flask
- PIL (Python Imaging Library)
- rembg
- Werkzeug

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/background-remover-web-app.git
    ```

2. Install the required dependencies:

    ```bash
    pip install Flask Pillow rembg
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd background-remover-web-app
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://localhost:5100/`.

4. Upload an image file (PNG, JPG, JPEG, or GIF) and click on the "Remove Background" button.

5. The background removed image will be downloaded automatically.

## Project Structure

- `app.py`: Main Flask application file.
- `uploads/`: Directory to store uploaded images.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for static files (CSS, JavaScript, etc.).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
