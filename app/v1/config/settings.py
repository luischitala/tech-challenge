import os
import environ 


_env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, '6CXIedt4nFvtFADJIAzB'),
    PORT=(int, 8000),
    USES_DOCKER=(str, 'No'),
)

if _env('USES_DOCKER') != 'Yes':
    environ.Env.read_env()

# Variables
DEBUG = _env('DEBUG')
SECRET_KEY = _env('SECRET_KEY')
PORT = _env('PORT')


