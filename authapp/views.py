from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
# Create your views here.


from authapp.forms import UserLoginForm, UserRegistrateForm, ChangeProfileForm
from authapp.models import User
from baskets.models import Basket




class Login(LoginView):
    template_name = 'authapp/login.html'
    redirect_field_name = reverse_lazy('mainapp:products')
    form_class = UserLoginForm




class CreateUser(CreateView):
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')
    form_class = UserRegistrateForm
    success_message = "Your profile was created successfully"


class Profile(UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    success_url = reverse_lazy('index')
    form_class = ChangeProfileForm
    success_message = "Your profile was update successfully"
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(User,pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context= super(Profile, self).get_context_data(**kwargs)
        context['baskets']= Basket.objects.filter(user=self.request.user)
        return context



class Logout(LogoutView):
    template_name = "index"