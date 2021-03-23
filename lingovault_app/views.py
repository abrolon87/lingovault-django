from django.shortcuts import render, redirect

from .models import Language, Post
from .forms import LanguageForm, PostForm
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


def new_post(request, language_id):
    language = Language.objects.get(id=language_id)

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.language = language
            new_post.save()
            return redirect('lingovault_app:language', language_id=language_id)

    context = {'language': language, 'form': form}
    return render(request, 'lingovault_app/new_post.html', context)


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    language = post.language

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lingovault_app:language', language_id=language.id)

    context = {'post': post, 'language': language, 'form': form}
    return render(request, 'lingovault_app/edit_post.html', context)
