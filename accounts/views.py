from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # 로그인된 상태가 보장됨
def profile(request):
    return render(request, 'accounts/profile.html')
