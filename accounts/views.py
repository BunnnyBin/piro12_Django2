from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login

from accounts.froms import SignupForm


@login_required  # 로그인된 상태가 보장됨
def profile(request):
    return render(request, 'accounts/profile.html')

'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #로그인 처리(회원가입과 동시에 로그인됨)
            auth_login(request, user)
            # 회원가입과 next
            next_url = request.GET.get('next') or 'profile'  # next 인자 가져오기 next가  없으면 profile
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
'''

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
    template_name = 'accounts/password_change_form.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')  # 성공하면 login으로 간다
    template_name = 'accounts/password_reset_form.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경 메일을 발송했습니다.')
        return super().form_valid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.info(self.request, '암호 리셋을 완료했습니다.')
        return super().form_valid(form)