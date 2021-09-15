

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xngvlz6u^fndts3m^5qj(gl90rh9a1((j*o+n77($m$0c63yln'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'comments_database',
        'USER': 'root',
        'PASSWORD':'Thispassword1',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
