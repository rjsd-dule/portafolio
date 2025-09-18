from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse
from app.models import Skill
from app.forms.SkillForm import SkillForm


def skill_list(request):
    skill = Skill.objects.all().order_by("name")
    return render(request, "skill/skill_list.html", {"skill": skill})


def skill_create(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect("skill_list")
    else:
        form = SkillForm()
    return render(request, "skill/skill_create.html", {"form": form})


@require_POST
def skill_delete(request, id):
    skill = get_object_or_404(Skill, id=id)
    skill.delete()
    return JsonResponse({"success": True, "message": "Registro Eliminado"})


@require_http_methods(["GET", "POST"])
def skill_update(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("skill_list")
    else:
        form = SkillForm(instance=skill)
    return render(request, "skill/skill_update.html", {"form": form})
