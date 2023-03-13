from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist
from .models import Speakers


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
        try:
            User.objects.get(email=request.POST['email'])
            return HttpResponse("Такой пользователь уже есть прикинь")
        except User.DoesNotExist:
            if request.POST['password'] == request.POST['password2']:
                user = User.objects.create_user(
                    email=request.POST['email'],
                    last_name=request.POST["last_name"],
                    first_name=request.POST['first_name'],
                    password=request.POST['password'])
                user.save()
                login(request, user)
                print('New user: ', user)
                return redirect('/')
    return render(request, 'register.html')


# def reset_password(request):
#     if request.method == 'POST':
#         try:
#             user = User.objects.get(email=request.POST["email"])
#             data = {
#                 "email": user.email,
#                 "domain": "DOMAIN",
#                 "site_name": "site_name",
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "user": user,
#                 "token": default_token_generator.make_token(user),
#                 "protocol": "http"
#             }
#
#
#         except User.DoesNotExist:
#             return redirect('/')


def htt(request):
    speakers = Speakers.objects.all()

    return render(request, "bg_img.html", {"speakers": speakers})


def publications(request):
    return render(request, "publications.html")


def organizers(request):
    return render(request, "organizers.html")


def registration_visa(request):
    return render(request, "registration_visa.html")

