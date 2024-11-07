from django.urls import path

from posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]
