from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated=models.BooleanField(default=True,db_index=True,verbose_name='Активирован?')
    messages=models.BooleanField(default=True,verbose_name='Слать оповещение о новых фильмах?')

    #кэшировать пароль
    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=4, decimal_places=1)
