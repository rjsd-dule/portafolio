from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms.PasswordUpdateForm import PasswordChangeCustomForm


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeCustomForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña actualizada correctamente")
            return redirect("perfil_user")
    else:
        form = PasswordChangeCustomForm(user=request.user)

    return render(request, "perfil/change_password.html", {"form": form})
