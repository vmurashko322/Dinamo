from django.shortcuts import render

def show_temp(request):
    return render(request, 'dinamo_page.html')
