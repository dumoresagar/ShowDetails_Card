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

# class ShowProduct(View):
#     def get(self,request):
#         product_list = Product.objects.all()
#         template_name = 'ProductApp/show_product.html'
#         context = {'product_list': product_list}
#         return render(request, template_name, context)

class ProductDetails(View):
    def get(self,request,i):
        product = Product.objects.get(id=i)
        template_name = 'ProductApp/product_details.html'
        context = {'product': product}
        return render(request, template_name, context)


from django.db.models import Q
from django.core.paginator import Paginator

# class ShowProduct(View):
#     def get(self, request):
#         query = request.GET.get('q')
#         if query:
#             # If there is a search query, filter the products based on the query
#             product_list = Product.objects.filter(
#                 Q(P_name__icontains=query) | Q(P_price__icontains=query)
#             )
#         else:
#             # If there's no search query, get all products
#             product_list = Product.objects.all()

#         template_name = 'ProductApp/show_product.html'
#         context = {'product_list': product_list, 'search_query': query}
#         return render(request, template_name, context)

class ShowProduct(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            # If there is a search query, filter the products based on the query
            product_list = Product.objects.filter(
                Q(P_name__icontains=query) | Q(P_price__icontains=query)
            )
        else:
            # If there's no search query, get all products
            product_list = Product.objects.all()

        # Create a Paginator object with 10 records per page
        paginator = Paginator(product_list, 5)

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')

        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)

        template_name = 'ProductApp/show_product.html'
        context = {'page_obj': page_obj, 'search_query': query}

        if not product_list.exists():  # Check if the product_list is empty
            context['not_found'] = True

        return render(request, template_name, context)




