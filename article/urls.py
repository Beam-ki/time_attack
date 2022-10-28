from django.urls import path,include
from article import views

urlpatterns = [
    path("",views.articleslist.as_view(), name="index"),
]
