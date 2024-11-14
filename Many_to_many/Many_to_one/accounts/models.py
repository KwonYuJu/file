from django.db import models
# Create your models here.
# AbstractUser : 로그인, 권한 관리 등에 필요한 기본적인 필드 제공
from django.contrib.auth.models import AbstractUser

# self : 재귀적으로 다대다 관계 형성
# symmentrical=False : 대칭 False -> 내가 팔로잉 했다고 상대방이 팔로우 한 건 아님
class User(AbstractUser):
  followings = models.ManyToManyField(
      'self', symmentrical=False, related_name='followers'
  )