from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='authors/')
    id_photo_front = models.ImageField('Удостоверение личности передняя часть', upload_to='authors/')
    id_photo_back = models.ImageField('Удостоверение личности задняя часть', upload_to='authors/' )
    birthdate = models.DateField('Дата рождения')
    profession = models.CharField('Профессия', max_length=255)
    portfolio = models.FileField('Портфолио',upload_to= 'app/',null=True)


    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
    class Meta:
        verbose_name = 'Чел'
        verbose_name_plural = 'Челы'
