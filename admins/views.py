import form as form
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import ProductCategoryForm, AdminCreateForm, AdminUpdateForm, ProductForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'geekbrains - admin',
    }
    return render(request, 'admin.html', context)


# CRUD for Users
@user_passes_test(lambda u: u.is_superuser)
def read_users(request):
    users = User.objects.all()
    context = {
        'title': 'geekbrains - админ, пользователи',
        'users': users
    }
    return render(request, 'CRUD user/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = AdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = AdminCreateForm()

    context = {
        'title': 'geekbrains - админ, создать пользователя',
        'form': form
    }
    return render(request, 'CRUD user/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, pk):
    user_select = User.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminUpdateForm(instance=user_select, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = AdminUpdateForm(instance=user_select)

    context = {
        'title': 'geekbrains - админ, изменить пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'CRUD user/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user.is_active = False
        user.save()
    return HttpResponseRedirect(reverse('admins:users'))


# CRUD for ProductCategory
@user_passes_test(lambda u: u.is_superuser)
def read_product_category(request):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'geekbrains - админ, категории',
        'categories': categories
    }
    return render(request, 'CRUD product_category/admin-product_category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def create_product_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('admins:categories'))
    else:
        form = ProductCategoryForm()

    context = {
        'title': 'geekbrains - админ, создать категорию',
        "form": form

    }
    return render(request, 'CRUD product_category/admin-product_category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_category(request, pk):
    category_select = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductCategoryForm(instance=category_select, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('admins:categories'))
    else:
        form = ProductCategoryForm(instance=category_select)

    context = {
        'title': 'geekbrains - админ, изменить категорию',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'CRUD product_category/admin-product_category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, pk):
    ProductCategory.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('admins:categories'))


# CRUD for Product
@user_passes_test(lambda u: u.is_superuser)
def read_products(request):
    products = Product.objects.all()
    context = {
        'title': 'geekbrains - админ, категории',
        'products': products
    }
    return render(request, 'CRUD product/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = ProductForm()

    context = {
        'title': 'geekbrains - админ, создать категорию',
        "form": form

    }
    return render(request, 'CRUD product/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, pk):
    product_select = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(instance=product_select, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = ProductForm(instance=product_select)

    context = {
        'title': 'geekbrains - админ, изменить категорию',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'CRUD product/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, pk):
    Product.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('admins:products'))
