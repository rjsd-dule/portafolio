from app.forms.RegisterForm import RegisterForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages


@require_http_methods(["POST", "GET"])
def register_user(request):
    try:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Usuario creado correctamente. Ya puedes iniciar sesión."
                )
                return redirect("login")
            else:
                return render(request, "auth/register.html", {"form": form})
        else:
            form = RegisterForm()
        return render(request, "auth/register.html", {"form": form})
    except Exception as e:
        print(e)
        messages.error(request, f"Ocurrió un error: {e}")
        form = RegisterForm()
        return render(request, "auth/register.html", {"form": form})
