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
    # new post
    path('new_post/<int:language_id>/', views.new_post, name='new_post'),
    # edit post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
