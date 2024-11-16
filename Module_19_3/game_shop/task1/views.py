from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

def checkup(username, password, repeat_password, age):
    buyers = Buyer.objects.all()
    if [buyer for buyer in buyers if buyer.name.lower() == username.lower()]:
        return 'Пользователь уже существует'
    if password != repeat_password:
        return 'Пароли не совпадают'
    if int(age) < 18:
        return 'Вы должны быть старше 18'
    return 'success'

def platform_view(request):
    title = 'Магазин'
    context = {
        'title': title,
        'main_page': 'Главная',
        'shop_page': 'Магазин',
        'cart_page': 'Корзина'
    }
    return render(request, 'platform.html', context)

def games_view(request):
    title = 'Игры'
    games = Game.objects.all()
    context = {
        'title': title,
        'main_page' : 'Главная',
        'shop_page' : 'Магазин',
        'cart_page' : 'Корзина',
        'games' : games
    }
    return render(request, 'games.html', context)

def cart_view(request):
    title = 'Корзина'
    context = {
        'title': title,
        'main_page': 'Главная',
        'shop_page': 'Магазин',
        'cart_page': 'Корзина',
        'items': ['Diablo III', 'Minecraft', 'Half-Life 2']
    }
    return render(request, 'cart.html', context)

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info['checkup'] = checkup(username, password, repeat_password, age)

            if info['checkup'] == 'success':
                Buyer.objects.create(name=username, balance=0, age=int(age))
                return HttpResponse(f'Приветствуем, {username}!"')
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page2.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        info['checkup'] = checkup(username, password, repeat_password, age)

        if info['checkup'] == 'success':
            Buyer.objects.create(name=username, balance=0, age=int(age))
            return HttpResponse(f'Приветствуем, {username}!"')
    return render(request, 'registration_page.html', info)
