from django.urls import path
from app.views import html, register, htt, publications, organizers, registration_visa
urlpatterns = [
    # path('login/', html),
    path('<filename>.html', html),
    path("register/", register, name="register"),
    path("", htt, name="home"),
    path("publications/", publications, name="publications"),
    path("organizers/", organizers, name="organizers"),
    path("registr-visa/", registration_visa, name="registration_visa")
]
