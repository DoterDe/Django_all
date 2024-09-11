
from django.db import models
from django.contrib.auth.models import User




class UserProfile(User):
    cv = models.FileField(upload_to='cv/photos')
    photo = models.ImageField(upload_to ='photo/photos' )
    id_photo = models.ImageField(upload_to = 'id_photo/photos')
