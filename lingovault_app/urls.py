from django.urls import path

from . import views

app_name = 'lingovault_app'

urlpatterns = [
    # home page
    path('', views.home, name='home'),
    # all languages
    path('languages/', views.languages, name='languages'),
    # page for individual language
    path('languages/<int:language_id>/', views.language, name='language'),
    # new language page
    path('new_language/', views.new_language, name='new_language'),
]
