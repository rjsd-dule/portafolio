from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from app.models import Category
from app.forms.CategoryForm import CategoryForm


@login_required
def category_list(request):
    categoria = Category.objects.all().order_by("name")
    return render(request, "categories/category_list.html", {"cat": categoria})


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "categories/category_create.html", {"form": form})


@require_POST
def category_delete(request, id):
    dl_category = get_object_or_404(Category, id=id)
    dl_category.delete()
    return JsonResponse({"success": True, "message": "Registro Eliminado"})


@require_http_methods(["GET", "POST"])
def category_update(request, id):
    up_category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=up_category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=up_category)
    return render(request, "categories/update_category.html", {"form": form})
