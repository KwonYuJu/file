from django.urls import path
from . import views

app_name='finlife'

urlpatterns = [
    path('', views.index, name="index"),
    path('finlife/save-deposit-products/', views.save_deposit_products, name='save_deposit_products')
]
