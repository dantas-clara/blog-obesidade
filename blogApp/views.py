from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dicionario_ctx = {
        'msg': "Vamos falar sobre "
    }

    return render(request, 'index/index.html', dicionario_ctx, status=200)
