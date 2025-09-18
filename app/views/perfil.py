from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
from app.models import User
from app.forms.ProfileForm import ProfileForm
from django.contrib import messages
from app.forms.PasswordUpdateForm import PasswordChangeCustomForm


@login_required
def perfil_user(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "perfil/user_profile.html", {"user": user})


@require_POST
def perfil_delete(request, id):
    return ""


@require_http_methods(["GET", "POST"])
def perfil_updated(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("perfil_user")
    else:
        form = ProfileForm(instance=user)
    return render(request, "perfil/user_profile.html", {"form": form})


@require_http_methods(["GET", "POST"])
@login_required
def perfil_update(request):
    user = get_object_or_404(User, id=request.user.id)

    profile_form = ProfileForm(
        request.POST or None, request.FILES or None, instance=user
    )
    password_form = PasswordChangeCustomForm(request.POST or None, user=user)

    if request.method == "POST":
        print("05")
        if "save_profile" in request.POST:
            print("06")
            if profile_form.is_valid():
                profile_form.save()
                # messages.success(request, "Perfil actualizado correctamente")
                return redirect("perfil_user")
        elif "change_password" in request.POST:
            print("005")
            if password_form.is_valid():
                password_form.save()
                # update_session_auth_hash(request, user)  # Mantiene sesión activa
                messages.success(request, "Contraseña actualizada correctamente")
                return redirect("perfil_user")

    return render(
        request,
        "perfil/user_profile.html",
        {"form": profile_form, "password_form": password_form, "user": user},
    )
