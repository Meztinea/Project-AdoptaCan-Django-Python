# Proyecto Personal de Django AdoptaCan 


### Se crea una aplicación web de adopción de perros.


## Instalación
~~~
python -m venv venv

# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
~~~

## Crear un superusuario para entrar al admin

~~~
python manage.py createsuperuser
~~~

## Base de datos: 
#### Este proyecto requiere tener instalado MySQL. Actualice los datos de la base de datos que quiere utilizar en settings.py.

~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_de_datos',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'host',
        'PORT': 'port'
    }
}
~~~

##### Documentación de Django para configuración de base de datos. https://docs.djangoproject.com/en/4.1/ref/settings/#databases

## Diagrama de Base de Datos: 


