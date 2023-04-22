from django.urls import path
from .views import index, about, shop, furniture,contacts

urlpatterns = [
    path('', index , name='index'),
    path('about/',about, name ='about'),
    path('shop/', shop, name='shop'),
    path('furniture/', furniture, name='furniture'),
    path('contacts', contacts, name='contacts'),
    

]