from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from app.models import Project
from app.forms.ProjectForm import ProjectForm


def project_list(request):
    project = Project.objects.all().order_by("category")
    print(project)
    return render(request, "project/project_list.html", {"project": project})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "project/project_create.html", {"form": form})


@require_POST
def project_delete(request, id):
    pro = get_object_or_404(Project, id=id)
    pro.delete()
    return JsonResponse({"success": True, "message": "Registro Eliminado"})


@require_http_methods(["POST", "GET"])
def project_update(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.user = request.user
            pro.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)

    return render(
        request, "project/project_update.html", {"form": form, "project": project}
    )
