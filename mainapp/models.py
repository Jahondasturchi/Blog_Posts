from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
    

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 500)
    created = models.DateTimeField(auto_now_add=True)