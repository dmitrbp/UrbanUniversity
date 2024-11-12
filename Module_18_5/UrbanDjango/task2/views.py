from django.shortcuts import render

# Create your views here.
def cview(request):
    return render(request, 'class_template.html')

def fview(request):
    return render(request, 'func_template.html')
