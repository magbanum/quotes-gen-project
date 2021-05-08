import random
from django.shortcuts import render
import random
from .models import Quote
from .forms import AddQuote

# Create your views here.
def home(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes)
    if request.method == 'POST':
        filled_form = AddQuote(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Thanks for contributing!'
            new_form = AddQuote()
            return render(request,'quotes/home.html', {'quotes':random_quote, 'addquote':new_form, 'note':note})
    else:   
        form = AddQuote()
        return render(request,'quotes/home.html', {'quotes':random_quote, 'addquote':form})