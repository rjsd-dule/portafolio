#Dule_developer
# Utiliza una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . .

RUN python manage.py collectstatic --noinput

# Expone el puerto
EXPOSE 8000

# Ejecuta el comando para iniciar el servidor de manera local
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Para Producion
CMD ["gunicorn", "portafolio.wsgi:application", "--bind", "0.0.0.0:8000"]