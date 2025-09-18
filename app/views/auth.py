from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms.LoginForm import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Has iniciado sesión correctamente")
                return redirect('home')
            else:
                messages.error(request, "Correo o contraseña incorrectos")
    else:
        form = LoginForm()

    response = render(request, "auth/login.html", {"form": form})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Has cerrado sesión correctamente")

    response = redirect('login')
    # Evitar cache de la página redirigida
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
