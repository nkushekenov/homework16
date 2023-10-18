from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import logging

def check_login(request):
    if 'login' not in request.GET:
        return redirect('another_page')
    else:
        return HttpResponse("Добро пожаловать, Вы вошли в личный кабинет.")
    
def another_page(request):
    return HttpResponse("Вы были перенаправлены сюда, потому что вы не вошли в систему.")


logger = logging.getLogger(__name__)

def log_request_data(request):
    logger.info(request)
    return HttpResponse("Запрошенные данные регистрируются.", status=200)

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")
