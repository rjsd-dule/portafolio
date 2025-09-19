from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods
from app.utils import AppData


def portafolio_view(request):
    data = AppData.AppData()
    return render(
        request,
        "public/base_portafolio.html",
        {
            "user": data.users,
            "project": data.projects,
            "pro": data.pro,
            "categories": data.categories,
            "exp": data.experiences,
            "skills": data.projects,
        },
    )


def portafolio_list(request):
    return render(request, "")


def portafolio_create(request):
    return render(request, "")


@require_POST
def portafolio_delete(request):
    return render(request, "")


@require_http_methods(["GET", "POST"])
def portafolio_update(request):
    return render(request, "")
