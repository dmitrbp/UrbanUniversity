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
    return render(request, 'games.html')

def cart_view(request):
    return render(request, 'cart.html')
