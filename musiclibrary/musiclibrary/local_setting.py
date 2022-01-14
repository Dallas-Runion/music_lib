SECRET_KEY = 'django-insecure-=*k#^eab@e=ldfigp2fg6()3(i6ci(sysvlw)b5nra#gwm1&qc'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
