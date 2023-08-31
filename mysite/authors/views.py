from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from .models import Author

@login_required
def create_author(request):
    if not request.user:
        return HttpResponse('Увійдіть у свій акаунт')
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(user=request.user, commit=False)
            return redirect('home')  # Повернення на головну сторінку
    else:
        form = AuthorForm()
    return render(request, 'authors/create_author.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'authors/author_detail.html', {'author': author})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return redirect('authors:author_list')






