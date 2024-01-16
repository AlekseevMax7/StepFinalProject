from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from goods.models import Categories

def index(request):

    context = {
        'title': 'Головна',
        'content': "Магазин автозапчастин",
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': "О нас",
    }

    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Контакти',
        'content': "Зв'яжіться з нами",
    }
    return render(request, 'main/contacts.html', context)

def delivery(request):
    context = {
        'title': 'Доставка та оплата',
        'content': "Інформація щодо доставки та оплати",
    }
    return render(request, 'main/delivery.html', context)