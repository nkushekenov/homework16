from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_login/', views.check_login, name='check_login'),
    path('another_page/', views.another_page, name='another_page'),
    path('log_request_data/', views.log_request_data, name='log_request_data'),

]
