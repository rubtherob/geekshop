from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
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




class CreateUser(FormView):
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')
    form_class = UserRegistrateForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_mail(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались!')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})

    def send_verify_mail(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        title = f'Подтверждение учетной записи {user.username}'
        message = f'Для подтверждения учетной записи {user.username} на портале \
        {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


    def verify(request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expired():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(request, user)
                return render(request, 'authapp/verification.html')
            else:
                print(f'error activation user: {user}')
                return render(request, 'authapp/verification.html')
        except Exception as e:
            print(f'error activation user : {e.args}')
            return HttpResponseRedirect(reverse('index'))


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
    template_name = "mainapp/index.html"