# Bizzbot 🤖 API

---

## Overview

BizzBot: Integrating a Truelens-powered chatbot with WhatsApp. Real-time data access, AI-driven customization, sales tracking, order reminders, payment handling. Transform customer interactions and optimize business operations seamlessly.


## Documentation 📃

You can find a detailed documentation of the API's endpoints [here](DOCUMENTATION.md)

## Technologies Used 🛠

- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- Django CORS Headers
- Python-Decouple
- Whitenoise
- DRF Yasg

## Getting Started ✨

Here are the steps to getting this API up and running:

1.  Open your favourite terminal and navigate to a suitable directory.  

    ```bash
    cd path/to/suitable/directory/
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/TegaRorobi/Bizzbot-backend.git
    ```

3. Navigate to the project directory
    ```bash
    cd Bizzbot-backend
    ```

4. Set up a virtual environment  
    - Windows

        ```bash
        python -m virtualenv venv
        venv\Scripts\activate
        ```
    - Mac / Linux

        ```bash
        python3 -m virtualenv venv
        source venv/bin/activate
        ```

5. Install the project's dependencies
    - Windows

        ```bash
        python -m pip install -r requirements.txt
        ```
    - Mac / Linux

        ```bash
        python3 -m pip3 install -r requirements.txt
        ```

6. Run a Local Development server on port 8000 (or any suitable port of your choice)
    - Windows

        ```bash
        python manage.py runserver
        ```
    - Mac / Linux

        ```bash
        python3 manage.py runserver
        ```

7. That's it 🎉. Start interacting with the endpoints, as detailed in the [documentation](DOCUMENTATION.md).

    Alternatively, if you have a local server running on port 8000,
    - You could use the swagger documentation (probably [here](http://localhost:8000/api/swagger/) or at `/api/swagger/` ).
    - You could use the redoc documentation (probably [here](http://localhost:8000/api/redoc/) or at `/api/redoc/` ).
    - You could also visit the endpoints URLs in the browsable API if you'd like.