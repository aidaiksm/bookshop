from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from .models import *
from .forms import SearchForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # pagination
    paginator = Paginator(products, 3)

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'page_obj': page_obj,
                                                      'page': page})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def about(request):
    return render(request, 'shop/about.html')


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.annotate(
            search=SearchVector('name', 'description'),
    ).filter(search=query)
    return render(request, 'shop/product/search.html', {'form': form,
                                                    'query': query,
                                                    'results': results})



class MainPageView(ListView):
    model = Product
    template_name = 'shop/product/index.html'
    context_object_name = 'products'
    paginate_by = 4