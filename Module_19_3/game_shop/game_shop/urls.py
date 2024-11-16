from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task1.views import platform_view, games_view, cart_view, sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('platform/', platform_view),
    path('platform/games/', games_view),
    path('platform/cart/', cart_view),
    path('html_sign_up/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]
