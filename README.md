1. Make sure Python is installed, and then install a virtual environment through python -m venv env
2. Once the virtual environment has been installed, activate it through .\env\Scripts\activate
3. Install requirements.txt using pip install -r requirements.txt
4. Run python manage.py makemigrations books
5. Run python manage.py migrate
6. Note that there are no books initally. I added a command to create dummy data for books (but with no images). To use this command run python manage.py seed
7. To run the server, use the command python manage.py runserver and go to the localhost, usually http://127.0.0.1:8000/
8. To add your own books, create an admin through python manage.py createsuperuser and then go to http://127.0.0.1:8000/admin and login
