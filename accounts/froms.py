from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


# 폼의 형식 규정
class SignupForm(UserCreationForm):
    # 폼에서 유효성 검사: 각 필드에 대한 validation, clean_필드명, clean
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format.'  #안내 메세지
        self.fields['username'].label = 'email'

    '''
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)  # 장고에서 지원하는 이메일 유효성 검사
        return value
    '''
    #email에도 작성한 이메일 값 반영하기
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user