#Dule_developer
# Utiliza una imagen base de Python
FROM python:3.10-slim-bullseye

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto
COPY . .

RUN python manage.py collectstatic --noinput

# Copia script de arranque
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expone el puerto
EXPOSE 8000

# Usa entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]