import random
from django.shortcuts import render

from .models import Quote


# Create your views here.


def home(request):
    quote = Quote.objects.all()
    random_quote = quote[random.randint(0, 240000)]
    colors = ['#FDF6F0', '#CDF0EA', '#F0E4D7', '#FFE194', '#FF96AD', '#FFF5DA', '#FCD8D4',
              '#FFF5B7', '#F8EDED', '#FFFFFF', '#EDFFEC', '#F9F3F3', '#FFE8E8', '#FFDCDC', '#F4F9F9', '#F3F2DA', '#F6F6F6', '#CFFFFE', '#D3DbFF', '#EDF492', '#FFD3E1']
    color = random.choice(colors)
    # print(random_quote)
    return render(request, 'quotes/home.html', {'quotes': random_quote, 'color': color})
