from django.shortcuts import render, redirect

from .models import Language
from .forms import LanguageForm
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


def new_language(request):
    if request.method != 'POST':
        form = LanguageForm()
    else:
        form = LanguageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lingovault_app:languages')
    context = {'form': form}
    return render(request, 'lingovault_app/new_language.html', context)
