from django.urls import path
from . import views

app_name = "lotto"

urlpatterns = [
    path("", views.lotto_input, name= "lotto"),
    path("result/", views.lotto_result, name= "result")
]