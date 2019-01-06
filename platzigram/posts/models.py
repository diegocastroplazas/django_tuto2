from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
""" Post models.
"""
class Post(models.Model):
    """[summary]
    
    Arguments:
        models {[type]} -- [description]
    """

    title = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'post/photos')
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
