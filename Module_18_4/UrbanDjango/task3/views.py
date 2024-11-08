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
        'game1': 'Atomic Heart',
        'game2': 'Cyberpunk 2077',
        'game3': 'PayDay 2'
    }
    return render(request, 'games.html', context)

def cart_view(request):
    title = 'Корзина'
    context = {
        'title': title,
        'pos1': 'Diablo III',
        'pos2': 'Minecraft',
        'pos3': 'Half-Life 2'
    }
    return render(request, 'cart.html', context)
