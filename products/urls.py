from django.urls import path

from . import views

urlpatterns = [
    path('', views.draft_list, name='draft_list'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('approve/<int:product_id>/', views.approve_product, name='approve_product'),
    path('approved/', views.approved_products, name='approved_products'),
]
