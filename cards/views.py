
from django.shortcuts import render

from .models import Card


def index(request, url_suffix):
    current_card = Card.objects.get(url_suffix=url_suffix)
    context = {'current_card': current_card}
    return render(request, 'cards/index.html', context)
