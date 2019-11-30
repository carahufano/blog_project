from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=200, verbose_name='Event Title')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    content     = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
