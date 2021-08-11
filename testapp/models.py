from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(verbose_name='사용자 닉네임', max_length=50)


class Player(models.Model):
    player_name = models.CharField(verbose_name='플레이어 이름', max_length=50)
    photo = models.ImageField(upload_to='player/', blank=True, null=True)
    attack = models.IntegerField(verbose_name='공격력')
    defense = models.IntegerField()
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE, blank=True, null=True)
    trade = models.ManyToManyField(User, related_name="trade", blank = True, null =True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(
        User, related_name='follower', blank=True)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    notyet = models.ManyToManyField(
        User, related_name='notyet', blank=True)
