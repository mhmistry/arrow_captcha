# Arrow CAPTCHA
A web-based CAPTCHA system using rotatable arrows to verify human users. Built with Django, HTML, CSS, and JavaScript, it provides an interactive and visually challenging verification step for login forms.

## Features
- Interactive Arrow CAPTCHA: Users click arrows to rotate them and match a target sequence of directions.
- Distorted Directions: The target directions are displayed as noisy, distorted text to prevent automated reading.
- Custom Validation: Only correct arrow rotations allow login.
- Seamless UX: CAPTCHA popup overlays the login page and closes automatically on success.
- Redirection: Upon successful verification, users are redirected to a “Signed In” page.
- Refresh Option: Users can generate a new target direction sequence without reloading the page.

## Installation
1. Clone the repository  
    ```bash
    git clone https://github.com/mhmistry/arrow_captcha.git  
    cd arrow_captcha

2. Create a virtual environment (optional but recommended)  
    ```bash
    python -m venv venv  
    venv\Scripts\activate # Windows  
    source venv/bin/activate # macOS/Linux

3. Install dependencies 
    ```bash
    pip install django

4. Run the server  
    ```bash
    python manage.py runserver

5. Open your browser and go to:  
    http://127.0.0.1:8000/

## Usage
1. Enter a username and password.
2. Check the "I'm not a robot" box to open the CAPTCHA.
3. Click the arrows to rotate them and match the distorted target directions.
4. Click Submit to verify.
5. Upon success, you are redirected to the signed-in page.

## Tech Stack
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default Django database)

## License
This project is open-source and free to use for educational purposes.
