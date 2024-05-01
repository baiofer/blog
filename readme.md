## BLOG

Proyecto creado con Django.

Para ponerlo en marcha, tras clonar el repo, accede a la carpeta del repo y activa el entorno virtual con:

```
cd blog
source blog-env/bin/activate
```

Ahora, realizamos las migraciones.

```
python3 manage.py migrate
```

Y finalmente, lanzamos la aplicación.

```
python3 manage.py runserver
```

En http://127.0.0.1:8000/, tendremos la aplicación lanzada.


