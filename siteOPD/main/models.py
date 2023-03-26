from django.db import models
from django.contrib.auth.models import User


class Recommendation(models.Model):
    about_problem = models.CharField('Введите название проблемы', max_length=50)
    help = models.CharField('Как решить проблему', max_length=500)

    def __str__(self):
        return self.about_problem

    class Meta:
        verbose_name = 'Рекоммендация'
        verbose_name_plural = 'Рекомендации'


class Interests(models.Model):
    interests = models.CharField('Интересы', max_length=50)

    def __str__(self):
        return self.interests

    class Meta:
        verbose_name_plural = "Интересы"


class Activity(models.Model):
    activity = models.CharField('Род деятельности', max_length=50)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = "Род деятельности"


class Friends(models.Model):
    friends = models.ForeignKey(User, on_delete=models.PROTECT)
    friends_name = models.CharField('Имя друга', max_length=50)
    friends_sec_name = models.CharField('Фамилия друга', max_length=50)
    friends_interests = models.ForeignKey(Interests, on_delete=models.PROTECT)
    friends_activity = models.ForeignKey(Activity, on_delete=models.PROTECT)

    def __str__(self):
        return self.friends_name

    class Meta:
        verbose_name_plural = "Друзья"



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_name = models.CharField('Имя пользователя', max_length=50)
    user_sec_name = models.CharField('Фамилия пользователя', max_length=50)
    interests = models.ForeignKey(Interests, on_delete=models.PROTECT)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = "Пользователи"