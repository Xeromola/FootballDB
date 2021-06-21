from django.urls import path
from footballDb import views

urlpatterns = [
    path('', views.home),
    path('centerforward', views.centerforward),
    path('secondstriker', views.secondstriker),
    path('leftwinger', views.leftwinger),
    path('rightwinger', views.rightwinger)
]
