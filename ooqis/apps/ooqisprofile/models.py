from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class OoqisProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.ooqisprofile = property(lambda u:OoqisProfile.objects.get_or_create(user=u)[0])
