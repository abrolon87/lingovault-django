from django.urls import path

from . import views

app_name = 'lingovault_app'

urlpatterns = [
    # home page
    path('', views.home, name='home'),
]
