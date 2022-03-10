import form as form
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse,reverse_lazy
from ordersapp.forms import OrderForm
from admins.forms import ProductCategoryForm, AdminCreateForm, AdminUpdateForm, ProductForm
from authapp.models import User
from mainapp.models import ProductCategory, Product
from ordersapp.models import Order
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import connection
from django.db.models import F


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

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(price=F('price') * (1 - discount / 100))
                db_profile_by_type(self.__class__, 'UPDATE', connection.queries)
        return super().form_valid(form)

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(EditCategory, self).dispatch(request,*args,**kwargs)


class DeleteCategory(DeleteView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name= 'CRUD product_category/admin-product_category-update-delete.html'
    success_url = reverse_lazy('admins:categories')
    context_object_name = 'category'

    def delete(self,request,*args,**kwargs):
        self.object= self.get_object()
        self.object.is_active= False
        self.object.save()
        return HttpResponseRedirect(self.success_url)



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

    def delete(self,request,*args,**kwargs):
        self.object= self.get_object()
        self.object.is_active= False
        self.object.save()
        return HttpResponseRedirect(self.success_url)

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

class ReadOrders(ListView):
    model = Order
    template_name = 'Update Status Orders/admin-order-read.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(ReadOrders, self).get_context_data()
        if self.kwargs:
            context['orders'] = Order.objects.filter(user=self.kwargs['pk'])
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ReadOrders, self).dispatch(request, *args, **kwargs)

class EditOrder(UpdateView):
    model = Order
    form_class = OrderForm
    template_name= 'Update Status Orders/admin-order-update-delete.html'
    success_url = reverse_lazy('admins:users')
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(EditOrder, self).get_context_data()
        if self.kwargs:
            context['order'] = Order.objects.get(id=self.kwargs['pk'])
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(EditOrder, self).dispatch(request,*args,**kwargs)


def db_profile_by_type(prefix, type, queries):
   update_queries = list(filter(lambda x: type in x['sql'], queries))
   print(f'db_profile {type} for {prefix}:')
   [print(query['sql']) for query in update_queries]

@receiver(pre_save, sender=ProductCategory)
def product_is_active_update_productcategory_save(sender, instance, **kwargs):
   if instance.pk:
       if instance.is_active:
           instance.product_set.update(is_active=True)
       else:
           instance.product_set.update(is_active=False)

       db_profile_by_type(sender, 'UPDATE', connection.queries)