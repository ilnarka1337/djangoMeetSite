from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.detail import DetailView
from .utils import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


class ProfileDetailView(LoginReqMixin, DetailView):
    model = MeetsUser
    context_object_name = 'app_user'
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data()
        return context
