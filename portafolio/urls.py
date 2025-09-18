"""
URL configuration for portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import (
    auth,
    register_user,
    home,
    portafolio,
    experience,
    category,
    skill,
    project,
    perfil,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", portafolio.portafolio_view, name="portafolio_view"),
    path("login", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
    path("register/", register_user.register_user, name="register_user"),
    path("home/", home.dashboard, name="home"),
    path("profile/", perfil.perfil_update, name="perfil_user"),
    path("profile/edit/", perfil.perfil_update, name="profile_update"),
    path("categories/", category.category_list, name="category_list"),
    path("categories/new/", category.category_create, name="category_create"),
    path("categories/<int:id>/edit/", category.category_update, name="category_update"),
    path(
        "categories/<int:id>/delete/", category.category_delete, name="category_delete"
    ),
    path("skills/", skill.skill_list, name="skill_list"),
    path("skills/new/", skill.skill_create, name="skill_create"),
    path("skills/<int:id>/edit/", skill.skill_update, name="skill_update"),
    path("skills/<int:id>/delete/", skill.skill_delete, name="skill_delete"),
    path("experience/", experience.experience_list, name="experience_list"),
    path("experience/new/", experience.experience_create, name="experience_create"),
    path(
        "experience/<int:id>/edit/",
        experience.experience_update,
        name="experience_update",
    ),
    path(
        "experience/<int:id>/delete/",
        experience.experience_delete,
        name="experience_delete",
    ),
    path("project/", project.project_list, name="project_list"),
    path("project/new/", project.project_create, name="project_create"),
    path("project/<int:id>/edit/", project.project_update, name="project_update"),
    path("project/<int:id>/delete/", project.project_delete, name="project_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
