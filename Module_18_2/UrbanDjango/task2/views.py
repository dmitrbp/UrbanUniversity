from django.shortcuts import render

# Create your views here.
def classview(request):
    return render(request, 'class_template.html')

def funcview(request):
    return render(request, 'func_template.html')
