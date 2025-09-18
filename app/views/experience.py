from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from app.models import Experience
from app.forms.ExperienceForm import ExperienceForm


@login_required
def experience_list(request):
    exp = Experience.objects.all().order_by("start_date")
    return render(request, "experience/experience_list.html", {"exp": exp})


def experience_create(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            return redirect("experience_list")
    else:
        form = ExperienceForm()
    return render(request, "experience/experience_create.html", {"form": form})


@require_POST
def experience_delete(request, id):
    exp = get_object_or_404(Experience, id=id)
    exp.delete()
    return JsonResponse({"success": True, "message": "Registro Eliminado"})


@require_http_methods(["GET", "POST"])
def experience_update(request, id):
    exp = get_object_or_404(Experience, id=id)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect("experience_list")
    else:
        form = ExperienceForm(instance=exp)
    return render(request, "experience/experience_update.html", {"form": form})
