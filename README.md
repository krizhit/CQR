**CQR Codes with Django Demo**

This project explores two creative approaches to injecting color into QR codes and showcases them within a simple Django application.

**Features:**

  - **Colorized QR Code Generation:** Choose between two methods to create visually appealing QR codes:
      - **Octal Representation:** A unique approach that maps ASCII characters to their corresponding octal values, assigning specific colors (CMY, RGB, black, white) based on this mapping.
      - **Pixel Merging:** Combines three black or white pixels into a single colored pixel, effectively reducing pixels required thus leaving space for more data to be stored by current calculations more than 3x the data in a generic qr-code.
  - **Interactive Django Demo:** A user-friendly Django application allows you to:
      - Enter the data you want to encode in the QR code.
      - Click a button to generate and display the corresponding colorized QR code.

**Requirements:**

  - Python 3.x
  - Django (installation instructions: [https://docs.djangoproject.com/en/4.2/intro/install/](https://www.google.com/url?sa=E&source=gmail&q=https://docs.djangoproject.com/en/4.2/intro/install/))
  - A QR code generation library (e.g., `python-qrcode` or `pypng`)

**Installation:**

1.  Clone this repository: `git clone https://your-repo-url.git`
2.  Create a virtual environment (recommended):
      - Linux/macOS: `python3 -m venv venv`
      - Windows: `python -m venv venv`
3.  Activate the virtual environment:
      - Linux/macOS: `. venv/bin/activate`
      - Windows: `venv\Scripts\activate`
4.  Install dependencies: `pip install -r requirements.txt` (create `requirements.txt` if missing)

**Usage:**

1.  Run the Django development server: `python manage.py runserver`
2.  Open your browser and navigate to http://127.0.0.1:8000/ (or your local development URL).
3.  Enter your desired data in the input field.
4.  Select the colorization method you prefer from the dropdown menu.
5.  Click "Generate QR Code" to see the colorized QR code.

**Code Structure:**

  - `qr_colorizer.py`: Functions for colorizing QR codes.
  - `qr_code_app`: The Django app directory containing models, views, and templates.
      - `views.py`: Handles user input, and renders the generated QR code within a template.
      - `templates/qr_code_app/`: HTML templates for the app's functionality.
  - `requirements.txt`: Lists the required Python libraries.

**Customization:**

  - Modify the color mapping in `qr_colorizer.py` to tailor the color scheme to your preferences.
  - Enhance the Django app by adding features like user input validation, error handling, or interactive styling elements.




