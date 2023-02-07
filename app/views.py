from django.shortcuts import render, redirect
from app.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist


def index(request):
    if request.user.is_anonymous:
        return redirect("/login.html")

    return render(request, 'index.html')


def html(request, filename):
    context = {"filename": filename,
               "collapse": ""}
    if request.user.is_anonymous and filename != "login":
        return redirect("/login.html")
    if filename == "logout":
        logout(request)
        return redirect("/")
    if filename == "login" and request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            if "@" in email:
                user = User.objects.get(email=email)
            else:
                user = User.objects.get(email=email)
            user = authenticate(request, email=user.email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

        print("login")
        print(email, password)
    print(filename, request.method)
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)


def register(request):
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
    return render(request, "register.html", {"user": User})
