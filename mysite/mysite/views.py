from django.shortcuts import render
from quotes.forms import QuoteForm


def home_view(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    quote_form = QuoteForm()
    return render(request, 'mysite/home.html', {'username': username, 'quote_form': quote_form})
