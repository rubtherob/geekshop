import form as form
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse,reverse_lazy

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


class ReadUsers(ListView):
    model = User
    template_name= 'CRUD user/admin-users-read.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(ReadUsers, self).get_context_data()
        context['title'] = 'geekbrains - админ, пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ReadUsers, self).dispatch(request,*args,**kwargs)


class CreateUsers(CreateView):
    model = User
    form_class = AdminCreateForm
    template_name= 'CRUD user/admin-users-create.html'
    context_object_name = 'users'
    success_url = reverse_lazy('admins:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(CreateUsers, self).get_context_data()
        context['title'] = 'geekbrains - админ, создать пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateUsers, self).dispatch(request,*args,**kwargs)


class EditUsers(UpdateView):
    model = User
    form_class = AdminUpdateForm
    template_name= 'CRUD user/admin-users-update-delete.html'
    context_object_name = 'users'
    success_url = reverse_lazy('admins:users')


    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(EditUsers, self).get_context_data()
        context['title'] = 'geekbrains - админ, изменить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(EditUsers, self).dispatch(request,*args,**kwargs)



class DeleteUsers(DeleteView):
    model = User
    form_class = AdminUpdateForm
    template_name= 'CRUD user/admin-users-update-delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('admins:users')

    def delete(self,request,*args,**kwargs):
        self.object= self.get_object()
        self.object.is_active= False
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(DeleteUsers, self).get_context_data()
        context['title'] = 'geekbrains - админ, удалить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteUsers, self).dispatch(request,*args,**kwargs)




# CRUD for ProductCategory
class ReadProductCategory(ListView):
    model = ProductCategory
    template_name= 'CRUD product_category/admin-product_category-read.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(ReadProductCategory, self).get_context_data()
        context['title'] = 'geekbrains - админ, категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ReadProductCategory, self).dispatch(request,*args,**kwargs)



class CreateProductCategory(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name= 'CRUD product_category/admin-product_category-create.html'
    success_url = reverse_lazy('admins:categories')


    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(CreateProductCategory, self).get_context_data()
        context['title'] = 'geekbrains - админ, создать категорию'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateProductCategory, self).dispatch(request,*args,**kwargs)


class EditCategory(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name= 'CRUD product_category/admin-product_category-update-delete.html'
    success_url = reverse_lazy('admins:categories')
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(EditCategory, self).get_context_data()
        context['title'] = 'geekbrains - админ, изменить категорию'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(EditCategory, self).dispatch(request,*args,**kwargs)


class DeleteCategory(DeleteView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name= 'CRUD product_category/admin-product_category-update-delete.html'
    success_url = reverse_lazy('admins:categories')
    context_object_name = 'category'



    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(DeleteCategory, self).get_context_data()
        context['title'] = 'geekbrains - админ, удалить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteCategory, self).dispatch(request,*args,**kwargs)



# CRUD for Product
class ReadProduct(ListView):
     model = Product
     template_name= 'CRUD product/admin-product-read.html'
     context_object_name = 'products'

     def get_context_data(self, *, object_list=None, **kwargs):
         context= super(ReadProduct, self).get_context_data()
         context['title'] = 'geekbrains - админ, продукты'
         return context

     @method_decorator(user_passes_test(lambda u: u.is_superuser))
     def dispatch(self, request, *args, **kwargs):
         return super(ReadProduct, self).dispatch(request,*args,**kwargs)


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name= 'CRUD product/admin-product-create.html'
    success_url = reverse_lazy('admins:products')


    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(CreateProduct, self).get_context_data()
        context['title'] = 'geekbrains - админ, создать продукт'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateProduct, self).dispatch(request,*args,**kwargs)



class EditProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name= 'CRUD product/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:products')
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(EditProduct, self).get_context_data()
        context['title'] = 'geekbrains - админ, изменить продукт'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(EditProduct, self).dispatch(request,*args,**kwargs)




class DeleteProduct(DeleteView):
    model = Product
    form_class = ProductForm
    template_name= 'CRUD product/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:products')
    context_object_name = 'product'



    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(DeleteProduct, self).get_context_data()
        context['title'] = 'geekbrains - админ, удалить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteProduct, self).dispatch(request,*args,**kwargs)