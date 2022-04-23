from django.shortcuts import render,redirect
from .forms import ProductModelForm
from .models import Product
from django.views import View




class AddProductView(View):
    def get(self,request):
        form = ProductModelForm()
        template_name = 'ProductApp/product.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = ProductModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_product")
        template_name = 'ProductApp/product.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowProduct(View):
    def get(self,request):
        product_list = Product.objects.all()
        template_name = 'ProductApp/show_product.html'
        context = {'product_list': product_list}
        return render(request, template_name, context)

class ProductDetails(View):
    def get(self,request,i):
        product = Product.objects.get(id=i)
        template_name = 'ProductApp/product_details.html'
        context = {'product': product}
        return render(request, template_name, context)






