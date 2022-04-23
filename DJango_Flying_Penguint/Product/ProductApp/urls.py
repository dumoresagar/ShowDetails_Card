from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.AddProductView.as_view(),name='add_product'),
    path('show/',views.ShowProduct.as_view(),name='show_product'),
    path('details/<int:i>/',views.ProductDetails.as_view(),name='details')
]

