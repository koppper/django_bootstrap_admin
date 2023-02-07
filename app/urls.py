from django.urls import path
from app.views import index, html, register
urlpatterns = [
    path('', index),
    # path('login/', html),
    path('<filename>.html', html),
    path("register/", register, name="register")
]
