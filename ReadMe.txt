Installation in Django Python

>>>Installation Python
 ->https://www.python.org/downloads/

>>For Windows OS 
 -Download python from windows store
 -Select the Python's version to download.
 -Click on the Install Now
 -Installation in Process

>>For Linux OS
 -sudo apt update
 -sudo apt install python3
	
>>>Open terminal
 -python --version
 
>>>To check pip version  
  -py -m pip --version
  -upgrade pip
  -py -m pip install --upgrade pip

>>>Installing virtualenv	
  #linux & mac os
   ->python3 -m pip install --user virtualenv
  #Windows
  ->py -m pip install --user virtualenv


>>>Create Virtual Environment
  #linux & mac os
  ->python3 -m venv environment_name
  #Windows
  ->python -m venv environment_name

>>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
 
>>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
>>>First please check Django properly Installed or not
 #Linux/macOS
 python3 -m django --version
 #Windows
 python  -m django --version

>>>Open terminal 
 -Goto project directory using cd command
 

>>>Install few libraries
->pip install django-embed-video
->pip install django-session-timeout
->pip install django-password-validators
->pip install django-js-routes
->pip install django-crispy-forms

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'Your Database Name',
        'USER' : 'Database User Name',
        'PASSWORD' : 'Your Password',
        'HOST' : "Write down Host",
        'PORT' : 'Write down port',
                
    }
}
>>>To Create superuser 
->python manage.py createsuperuser
	enter username = your_username
	enter your Email Address
	enter your password
	enter your password again 
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>To load Static Files:-
>Go to Skote/setings.py
-Add following command:-
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT= os.path.join(BASE_DIR,'assets')

>Run Command In Terminal
-python manage.py collectstatic
	 
     
>>>To Set Default Layout
 >Goto templates/partial/base.html


>>> Migrate Model 
-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate

>>>Run your project
-Windows:-python manage.py runserver
-Linux:-python3 manage.py runserver
