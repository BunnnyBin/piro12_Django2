from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login

@login_required  # 로그인된 상태가 보장됨
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #로그인 처리
            auth_login(request, user)
            # 회원가입과 next
            next_url = request.GET.get('next') or 'profile'  # next 인자 가져오기 인자 없으면 profile
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

'''
signup = CreateView.as_view(model=User, form_class=UserCreationForm,
                            success_url='settings.LOGIN_URL',
                            template_name='accounts/signup.html')
'''