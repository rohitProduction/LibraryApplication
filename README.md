1. Make sure Python is installed, and then install a virtual environment through python -m venv env
2. Once the virtual environment has been installed, activate it through .\env\Scripts\activate
3. Install requirements.txt using pip install -r requirements.txt
4. Run python manage.py makemigrations books
5. Run python manage.py migrate
6. To run the server, use the command python manage.py runserver and go to the localhost, usually http://127.0.0.1:8000/
7. At first, the database is empty, therefore create an admin through python manage.py createsuperuser and then go to http://127.0.0.1:8000/admin and login. There are no books available, so to test the website out, please add your own books.
