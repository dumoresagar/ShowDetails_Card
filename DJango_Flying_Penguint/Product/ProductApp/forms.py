from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'PRODUCT IMAGE':'Pdf,Doc,Docx',
            'PRODUCT PRICE':'Enter Product Price',
            'PRODUCT NAME':'Enter Product Name',
        }
