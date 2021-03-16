from django.shortcuts import render

from .models import Language
# Create your views here.


def home(request):
    return render(request, 'lingovault_app/home.html')


def languages(request):
    languages = Language.objects.order_by('date_added')
    context = {'languages': languages}
    return render(request, 'lingovault_app/languages.html', context)


def language(request, language_id):
    language = Language.objects.get(id=language_id)
    posts = language.post_set.order_by('-date_added')
    context = {'language': language, 'posts': posts}
    return render(request, 'lingovault_app/language.html', context)
