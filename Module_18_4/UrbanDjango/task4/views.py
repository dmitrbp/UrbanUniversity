from django.shortcuts import render

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
    context = {
        'title': title,
        'main_page': 'Главная',
        'shop_page': 'Магазин',
        'cart_page': 'Корзина',
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Diablo III']
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
