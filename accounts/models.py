from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)


# 회원가입(user 생성)과 동시에 프로필 만들기
def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        #가입시기
        user = kwargs['instance']
        Profile.objects.create(user=user)

        #환영 이메일 보내기기


# sinals-> post_save(호출 함수, 관련 모델): save() 직후에 호출
post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
