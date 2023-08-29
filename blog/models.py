from django.db import models
from django.contrib.auth.models import User

class Blog_Post(models.Model):
    '''
    This block of code creates a blog post form users,
    also deletes all posts linked to a user if user acc is deleted
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.blog_title
