from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm
from .models import Quote

@login_required
def add_quote(request):
    if not request.user:
        return HttpResponse('Увійдіть у свій акаунт')
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save(user=request.user, commit=False)
            return redirect('home')  # Повернення на головну сторінку
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})