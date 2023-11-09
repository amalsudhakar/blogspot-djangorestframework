# Django Rest Framework Blog App

This repository contains a simple blog app built using Django Rest Framework for the backend and HTML for the frontend.

## Prerequisites

Make sure you have the following installed before running the application:

- Python (version 3.11.4)
- Django
- Django Rest Framework

## Installation

1. Clone the repository:

    git clone https://github.com/amalsudhakar/blogspot-djangorestframework.git

2. Navigate to the project directory:

    cd Blog

3. Create and activate a virtual environment to isolate the project dependencies:

    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

4. Create a .env file in the root of the project and set the SECRET_KEY variable. You can generate a Django secret key using a tool like Djecrety.

    Example .env file:

    SECRET_KEY=your_secret_key_here

5. Install the requirements:

    pip install -r requirements.txt

## Running the Application
1. Apply migrations:

    python manage.py migrate

2. Run the Django development server:

    python manage.py runserver
    
    The backend API will be accessible at http://localhost:8000/

3. Open another terminal window, navigate to the templates folder, and run your HTML file using a local server. Replace <your-port> with the desired port number:

    cd templates
    python -m http.server <your-port>
    
    The frontend HTML can be accessed at http://localhost:<your-port>/index.html