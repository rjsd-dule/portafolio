from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from app.utils import AppData


@login_required(login_url="login")
@never_cache
def dashboard(request):
    data = AppData.AppData()
    dtObject = data.counts()

    context = {"user": request.user, "dt": dtObject}
    response = render(request, "dashboard.html", context)
    response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response
