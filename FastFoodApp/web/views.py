from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import RequestContext
from FastFoodApp.products.models import Product

UserModel = get_user_model()


def index(request):
    user = request.user
    context = {
        "UserModel": UserModel,
        "user": user
    }
    return render(request, "common/index.html", context)


def menu(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 5)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)

    context = {'products': products, 'page_obj': page_obj}
    return render(request, "common/menu.html", context)


def custom_404(request, exception):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response
