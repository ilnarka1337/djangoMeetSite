from django.contrib.auth.mixins import LoginRequiredMixin


class LoginReqMixin(LoginRequiredMixin):
    login_url = '/login/'

    redirect_field_name = 'login/'
