from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2', 'user3']


def checkup(username, password, repeat_password, age):
    if [user for user in users if user.lower() == username.lower()]:
        return 'Пользователь уже существует'
    if password != repeat_password:
        return 'Пароли не совпадают'
    if int(age) < 18:
        return 'Вы должны быть старше 18'
    return 'success'

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

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Age: {age}')

        if info['checkup'] == 'success':
            return HttpResponse(f'Приветствуем, {username}!"')
    return render(request, 'registration_page.html', info)
