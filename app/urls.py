from django.urls import path
from app.views import index, html, register, htt
urlpatterns = [
    path('', index),
    # path('login/', html),
    path('<filename>.html', html),
    path("register/", register, name="register"),
    path("ht/", htt)
]
