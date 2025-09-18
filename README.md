# PortfolioHub

Plataforma web donde los usuarios pueden crear, personalizar y gestionar su portafolio profesional desde un dashboard moderno e interactivo.

---

## Descripción

PortfolioHub permite a los usuarios diseñar su portafolio personal de manera sencilla y visual. Cada usuario tiene un dashboard donde puede:

* Añadir secciones como Experiencia, Habilidades y Proyectos.
* Personalizar el diseño y la apariencia de su portafolio.
* Compartir su portafolio profesional con un enlace único.

El objetivo de PortfolioHub es **facilitar la creación de portafolios profesionales sin necesidad de conocimientos técnicos**, ofreciendo una experiencia intuitiva y elegante para cualquier usuario.

---

## Requisitos

* Python 3.11.2
* Django 5.2
* Gunicorn 21.2.0

---

## Instalación y configuración

1. Clona el repositorio:

```bash
git clone https://github.com/rjsd-dule/portafolio.git
cd portafolio
```

2. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

3. Aplica las migraciones de la aplicación:

```bash
python manage.py makemigrations app
python manage.py migrate
```

## Ejecución en local

```bash
python manage.py runserver
```

Abre tu navegador en: `http://127.0.0.1:8000/`

---
