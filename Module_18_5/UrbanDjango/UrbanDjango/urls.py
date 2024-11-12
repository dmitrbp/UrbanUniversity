from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task2.views import cview, fview
# cview = importlib.import_module('UrbanDjango.task2.views.cview')
# fview = importlib.import_module('UrbanDjango.task2.views.fview')
from task4.views import platform_view, games_view, cart_view
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('class/', cview),
    path('func/', fview),
    path('platform/', platform_view),
    path('platform/games/', games_view),
    path('platform/cart/', cart_view),
    path('html_sign_up/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]
